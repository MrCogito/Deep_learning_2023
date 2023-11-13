import torch
import torch.nn as nn
from torch.functional import F
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch_geometric.utils import scatter

class PaiNN(nn.Module):
    def __init__(self, num_atoms, num_embeddings, cutoff_dist):
        super().__init__()
        self.num_embeddings = num_embeddings
        self.cutoff_dist = cutoff_dist

        self.embeddings = nn.Embedding(num_atoms, num_embeddings)

        # message block
        self.linear_phi1 = nn.Linear(self.num_embeddings, self.num_embeddings)
        self.linear_phi2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)
        self.linear_W = nn.Linear(20, 3*self.num_embeddings)

        # update block
        self.linear_U = nn.Linear(self.num_embeddings, self.num_embeddings)
        self.linear_V = nn.Linear(self.num_embeddings, self.num_embeddings)
        self.linear_update1 = nn.Linear(2*self.num_embeddings, self.num_embeddings)
        self.linear_update2 = nn.Linear(self.num_embeddings, 3*self.num_embeddings)

    # equivariant_repr: [n_neighbours, num_embeddings, 3]
    # embeddings: [n_neighbours, num_embeddings]
    # rel_pos: [n_neighbours, 3]
    def message(self, equivariant_repr, embeddings, rel_pos):
        phi = self.linear_phi1(embeddings) # [n_neighbours, num_embeddings]
        phi = F.silu(phi)
        phi = self.linear_phi2(phi)       # [n_neighbours, 3*num_embeddings]

        distance = torch.norm(rel_pos, dim=1)   # [n_neighbours]
        RBF = torch.stack([torch.sin(torch.arange(1, 21) * torch.pi * dist / self.cutoff_dist) / dist for dist in distance]) # [n_neighbours, 20]
        W = self.linear_W(RBF) # [n_neighbours, 3*num_embeddings]
        # Add cosine cutoff # [n_neighbours, 3*num_embeddings]

        split = torch.mul(phi, W) # [n_neighbours, 3*num_embeddings]

        embeddings = split[:, :self.num_embeddings] # [n_neighbours, num_embeddings]
        embeddings = torch.sum(embeddings, dim=0)   # [num_embeddings]

        equivariant_repr = torch.mul(equivariant_repr, split[:, self.num_embeddings:2*self.num_embeddings, None]) \
                            + torch.mul(torch.mul(split[:, 2*self.num_embeddings:, None], rel_pos[:, None, :]), distance[:, None, None]) # [n_neighbours, num_embeddings, 3]
        equivariant_repr = torch.sum(equivariant_repr, dim=0) # [num_embeddings, 3]

        return equivariant_repr, embeddings

    # equivariant_repr: [n_neighbours, num_embeddings, 3]
    # embeddings: [n_neighbours, num_embeddings]
    def update(self, equivariant_repr, embedding):
        U = self.linear_U(equivariant_repr)
        V = self.linear_V(equivariant_repr) # [self.num_embeddings, 3]

        stack = torch.stack(embedding, torch.norm(V, dim=1))
        stack = self.linear_update1(stack)
        stack = F.silu(stack)
        split = self.linear_update2(stack)

        equivariant_repr = torch.mul(U, split[:self.num_embeddings])
        embedding = split[self.num_embeddings:2*self.num_embeddings] + torch.sum(U * V, dim=1) \
                     * split[2*self.num_embeddings]

        return equivariant_repr, embedding


    def forward(self, data):
        pos, z, neighbours = data.pos, data.z, data.neighbours

        embeddings = self.embeddings(z)
        equivariant_repr = torch.zeros((len(z), self.num_embeddings, 3))

        for i in torch.arange(len(z)):
            neighbours_idx = neighbours[i].nonzero(as_tuple=True)[0] # [batchsize num_neighbours]
            rel_pos = pos[i] - pos

            delta_equivariant_repr, delta_embedding = self.message(equivariant_repr[neighbours_idx], embeddings[neighbours_idx], rel_pos[neighbours_idx])
            equivariant_repr[i] += delta_equivariant_repr
            embeddings[i] += delta_embedding
            exit()

            # equivariant_repr[i], embeddings[i] += self.update(equivariant_repr[neighbours_idx], embeddings[neighbours_idx])

        return


if __name__ == "__main__":
    cutoff_dist = 5

    dataset = QM9(root=f"./data/{5}A")

    train, validation, test = torch.utils.data.random_split(dataset, [0.8, 0.1, 0.1], generator=torch.Generator().manual_seed(42))

    train_loader = DataLoader(train, batch_size=32)

    net = PaiNN(9, 128, cutoff_dist)
    net(next(iter(train_loader)))