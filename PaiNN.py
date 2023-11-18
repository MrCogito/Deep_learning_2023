import torch
import torch.nn as nn
from torch.functional import F
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch_geometric.utils import scatter
from torch_geometric.nn import MessagePassing


class Message(MessagePassing):
    def __init__(self, num_embeddings, cutoff_dist):
        super().__init__(flow="source_to_target")

        self.num_embeddings = num_embeddings
        self.cutoff_dist = cutoff_dist

        self.linear_phi1 = nn.Linear(self.num_embeddings, self.num_embeddings)
        self.linear_phi2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)
        self.linear_W = nn.Linear(20, 3*self.num_embeddings)


    # embeddings :      [natoms, num_embeddings]
    # equivar_repr :    [3, natoms, num_embeddings]
    # pos :             [natoms, 3]
    # batch :           [natoms]
    def forward(self, embeddings, equivar_repr, pos, batch):

        # count atoms in each molecule
        unique = torch.unique(batch, return_counts=True)
        # i-th row is for i-th atom in data.z, ij element is distance between i-th and j-th atom
        distances = torch.cdist(pos, pos, p=2)
        # select atoms
        neighbours = torch.where(distances <= self.cutoff_dist, 1, 0)
        # mask other atoms
        neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]])
        # exclude itself
        neighbours = neighbours - torch.eye(neighbours.shape[0])
        # get neighbours in the form of [2, num_edges]
        neighbours = neighbours.nonzero(as_tuple=False).t()
        neighbours = torch.index_select(neighbours, 0, torch.LongTensor([1,0])).type(torch.LongTensor)

        return self.propagate(neighbours, s=embeddings, v=equivar_repr, r=pos, neighbours=neighbours)

    # _j is a neighbour, _i is the atom
    # s_j : [num_edges, num_embeddings]
    # v_j : [3, num_edges, num_embeddings]
    # r_i : [num_edges, 3]
    # r_j : [num_edges, 3]
    def message(self, s_j, v_j, r_i, r_j, neighbours):
        # 1. calculate phi
        phi = self.linear_phi1(s_j) # [num_edges, num_embeddings]
        phi = F.silu(phi)
        phi = self.linear_phi2(phi) # [num_edges, 3*num_embeddings]

        rel_pos = r_i - r_j         # [num_edges, 3]
        distance = torch.norm(rel_pos, dim=1) # [num_edges]
        RBF = torch.sin(torch.arange(1, 21)[None, :] * torch.pi * distance[:, None] / self.cutoff_dist) / distance[:, None] # [num_edges, 20]
        W = self.linear_W(RBF)      # [num_edges, 3*num_embeddings]
        # Add cosine cutoff         # [num_edges, 3*num_embeddings]

        split = torch.mul(phi, W)   # [num_edges, 3*num_embeddings]

        delta_s_ij = split[:, :self.num_embeddings] # [num_edges, num_embeddings]

        v_j = v_j.permute([1,2,0]) # [num_edges, num_embeddings, 3]
        delta_v_ij = torch.mul(v_j, split[:, self.num_embeddings:2*self.num_embeddings, None]) \
                            + torch.mul(torch.mul(split[:, 2*self.num_embeddings:, None], rel_pos[:, None, :]), distance[:, None, None]) # [num_edges, num_embeddings, 3]

        return delta_s_ij, delta_v_ij

    def aggregate(self, message, s_j, v_j, r_i, r_j, neighbours):
        delta_s_ij, delta_v_ij = message

        delta_s_ij = scatter(delta_s_ij, neighbours[1], dim=0, reduce="sum") # [natoms, num_embeddings]
        delta_v_ij = scatter(delta_v_ij, neighbours[1], dim=0, reduce="sum") # [natoms, num_embeddings, 3]

        delta_v_ij = delta_v_ij.permute([2, 0, 1]) # [3, natoms, num_embeddings]

        return delta_s_ij, delta_v_ij

    def update(self, agg_message, s_j, v_j, r_i, r_j, neighbours):
        return agg_message

class PaiNN(nn.Module):
    def __init__(self, num_atoms, num_embeddings, cutoff_dist):
        super().__init__()
        self.num_embeddings = num_embeddings
        self.cutoff_dist = cutoff_dist

        self.embeddings = nn.Embedding(num_atoms, num_embeddings)

        # message block
        self.message = Message(self.num_embeddings, cutoff_dist)

        # update block
        # self.linear_U = nn.Linear(self.num_embeddings, self.num_embeddings)
        # self.linear_V = nn.Linear(self.num_embeddings, self.num_embeddings)
        # self.linear_update1 = nn.Linear(2*self.num_embeddings, self.num_embeddings)
        # self.linear_update2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)

    # # equivariant_repr: [n_neighbours, num_embeddings, 3]
    # # embeddings: [n_neighbours, num_embeddings]
    # def update(self, equivariant_repr, embedding):
    #     U = self.linear_U(equivariant_repr.permute(0,2,1))
    #     U = U.permute(0,2,1)
    #     print(f"U shape: ", U.shape)
    #     V = self.linear_V(equivariant_repr.permute(0,2,1)) # [self.num_embeddings, 3]
    #     V = V.permute(0,2,1)
    #     print(V.shape)
    #     print((torch.norm(V, dim=2)).shape)

    #     stack = torch.cat([embedding, torch.norm(V, dim=2)], dim=1)
    #     print(f"stack.shape", stack.shape)
    #     stack = self.linear_update1(stack)
    #     stack = F.silu(stack)
    #     split = self.linear_update2(stack)
    #     split1 = split[:, :self.num_embeddings]  # First part, contains the first 128 elements in the second dimension
    #     split2 = split[:, self.num_embeddings: 2*self.num_embeddings]  # Second part, contains the next 128 elements
    #     split3 = split[:, 2*self.num_embeddings:]  # Third part, contains the last 128 elements
    #     print(f"split1 size: ", split1.shape)
    #     print(f"split2 size: ", split2.shape)
    #     print(f"split3 size: ", split3.shape)
    #     split1_expanded = split1.unsqueeze(-1)
    #     equivariant_repr = torch.mul(U, split1_expanded)
    #     print(torch.sum(U * V, dim=2).shape)
    #     embedding = split2 + torch.sum(U * V, dim=2) \
    #                  * split3

    #     return equivariant_repr, embedding

    def forward(self, data):
        # 1. Initialize inputs (s and v)
        embeddings = self.embeddings(data.z) # [batch_size, num_embeddings]
        equivariant_repr = torch.zeros((3, len(data.z), self.num_embeddings))

        # 2. Send messages and make updates

        output = self.message(embeddings, equivariant_repr, data.pos, data.batch)


        # 3. Final linear layer

        return output


if __name__ == "__main__":
    ### load data
    dataset = QM9(root=f"./data/{5}A")

    # Calculate split lengths
    total_length = len(dataset)
    train_length = int(0.8 * total_length)
    val_length = int(0.1 * total_length)
    test_length = total_length - train_length - val_length

    # Perform random split
    train_set, val_set, test_set = torch.utils.data.random_split(dataset, [train_length, val_length, test_length], generator=torch.Generator().manual_seed(42))

    # Create data loaders
    train_loader = DataLoader(train_set, batch_size=32)
    val_loader = DataLoader(val_set, batch_size=32)
    test_loader = DataLoader(test_set, batch_size=32)


    ### Testing
    # Instantiate the PaiNN model
    model = PaiNN(num_atoms=9, num_embeddings=128, cutoff_dist=5) # Adjust the parameters as needed
    batch = next(iter(train_loader))
    print(batch)

    out = model(batch)
    print(out)

    # # Now you can check the dimensions and values of updated_equivariant_repr and updated_embedding
    # print("Updated Equivariant Representation Shape:", updated_equivariant_repr.shape)
    # print("Updated Embedding Shape:", updated_embedding.shape)
