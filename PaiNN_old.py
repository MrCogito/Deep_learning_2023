import torch
import torch.nn as nn
from torch.functional import F
from torch_geometric.utils import scatter
from torch_geometric.nn import MessagePassing

class GraphLayer(MessagePassing):
    def __init__(self, num_embeddings, cutoff_dist, device):
        super().__init__(flow="source_to_target")

        self.device = device

        self.num_embeddings = num_embeddings
        self.cutoff_dist = cutoff_dist

    # embeddings :      [natoms, num_embeddings]
    # equivar_repr :    [3, natoms, num_embeddings]
    # pos :             [natoms, 3]
    # batch :           [natoms]
    def forward(self, embeddings, equivar_repr, pos, batch):
        neighbours = self.get_neighbours_as_edge_index(pos, batch, self.cutoff_dist)

        return self.propagate(neighbours, s=embeddings, v=equivar_repr, r=pos, neighbours=neighbours)

    # _j is a neighbour, _i is the atom
    # s_i : [num_edges, num_embeddings]
    # v_i : [3, num_edges, num_embeddings]
    def aggregate(self, message, neighbours):
        delta_s_ij, delta_v_ij = message

        delta_s = scatter(delta_s_ij, neighbours[1], dim=0, reduce="sum") # [natoms, num_embeddings]
        delta_v = scatter(delta_v_ij, neighbours[1], dim=1, reduce="sum") # [3, natoms, num_embeddings]

        return delta_s, delta_v

    def update(self, agg_message, s, v):
        delta_s, delta_v = agg_message

        s += delta_s
        v += delta_v

        return s, v

    def get_neighbours_as_edge_index(self, pos, batch, cutoff_dist):
        # count atoms in each molecule
        unique = torch.unique(batch, return_counts=True)
        # i-th row is for i-th atom in data.z, ij element is distance between i-th and j-th atom
        distances = torch.cdist(pos, pos, p=2)
        # select atoms
        neighbours = torch.where(distances <= cutoff_dist, 1, 0)
        # mask other atoms
        neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
        # exclude itself
        neighbours = neighbours - torch.eye(neighbours.shape[0], device=self.device)
        # get neighbours in the form of [2, num_edges]
        neighbours = neighbours.nonzero(as_tuple=False).t()
        neighbours = torch.index_select(neighbours, dim=0, index=torch.tensor([1,0], device=self.device)).type(torch.LongTensor).to(self.device)

        return neighbours

class Message(GraphLayer):
    def __init__(self, num_embeddings, cutoff_dist, device):
        super().__init__(num_embeddings, cutoff_dist, device)

        self.linear_phi1 = nn.Linear(self.num_embeddings, self.num_embeddings)
        self.linear_phi2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)
        self.linear_W = nn.Linear(20, 3*self.num_embeddings)

    # _j is a neighbour, _i is the atom
    # s_j : [num_edges, num_embeddings]
    # v_j : [3, num_edges, num_embeddings]
    # r_i : [num_edges, 3]
    # r_j : [num_edges, 3]
    def message(self, s_j, v_j, r_i, r_j):
        phi = self.linear_phi1(s_j) # [num_edges, num_embeddings]
        phi = F.silu(phi)
        phi = self.linear_phi2(phi) # [num_edges, 3*num_embeddings]

        rel_pos = r_i - r_j         # [num_edges, 3]
        distance = torch.norm(rel_pos, dim=1) # [num_edges]
        cutoff = distance.detach().clone()
        cutoff[distance <= self.cutoff_dist] = 0.5*(torch.cos(torch.pi * distance[distance <= self.cutoff_dist] / self.cutoff_dist) + 1)
        cutoff[distance > 0] = 0
        RBF = cutoff[:, None] * torch.sin(torch.arange(1, 21, device=self.device)[None, :] * torch.pi * distance[:, None] / self.cutoff_dist) / distance[:, None] # [num_edges, 20]
        W = self.linear_W(RBF)      # [num_edges, 3*num_embeddings]

        split = torch.mul(phi, W)   # [num_edges, 3*num_embeddings]
        split1 = split[:, :self.num_embeddings]
        split2 = split[:, self.num_embeddings:2*self.num_embeddings]
        split3 = split[:, 2*self.num_embeddings:]

        delta_s_ij = split1 # [num_edges, num_embeddings]

        v_j = v_j.permute([1,2,0]) # [num_edges, num_embeddings, 3]
        delta_v_ij = torch.mul(v_j, split2[:, :, None]) \
                            + torch.mul(torch.mul(split3[:, :, None], rel_pos[:, None, :]), distance[:, None, None]) # [num_edges, num_embeddings, 3]
        delta_v_ij = delta_v_ij.permute([2, 0, 1]) # [3, natoms, num_embeddings]

        return delta_s_ij, delta_v_ij

class Update(GraphLayer):
    def __init__(self, num_embeddings, cutoff_dist, device):
        super().__init__(num_embeddings, cutoff_dist, device)

        self.linear_U = nn.Linear(self.num_embeddings, self.num_embeddings, bias=False)
        self.linear_V = nn.Linear(self.num_embeddings, self.num_embeddings, bias=False)
        self.linear_update1 = nn.Linear(2*self.num_embeddings, self.num_embeddings)
        self.linear_update2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)

    # _j is a neighbour, _i is the atom
    # s_j : [num_edges, num_embeddings]
    # v_j : [3, num_edges, num_embeddings]
    def message(self, s_j, v_j):
        U = self.linear_U(v_j) # [3, num_edges, num_embeddings]
        V = self.linear_V(v_j) # [3, num_edges, num_embeddings]

        stack = torch.cat([s_j, torch.norm(V, dim=0)], dim=1) # [num_edges, 2*num_embeddings]

        stack = self.linear_update1(stack) # [num_edges, num_embeddings]
        stack = F.silu(stack)
        split = self.linear_update2(stack) # [num_edges, 3*num_embeddings]

        split1 = split[:, :self.num_embeddings]  # First part, contains the first 128 elements in the second dimension
        split2 = split[:, self.num_embeddings: 2*self.num_embeddings]  # Second part, contains the next 128 elements
        split3 = split[:, 2*self.num_embeddings:]  # Third part, contains the last 128 elements

        delta_s_ij = split2 + torch.sum(U * V, dim=0) * split3 # [num_edges, num_embeddings]

        delta_v_ij = torch.mul(U, split1[None, :, :]) # [3, num_edges, num_embeddings]

        return delta_s_ij, delta_v_ij