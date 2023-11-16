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
        U = self.linear_U(equivariant_repr.permute(0,2,1))
        U = U.permute(0,2,1)
        print(f"U shape: ", U.shape)
        V = self.linear_V(equivariant_repr.permute(0,2,1)) # [self.num_embeddings, 3]
        V = V.permute(0,2,1)
        print(V.shape)
        print((torch.norm(V, dim=2)).shape)
        
        stack = torch.cat([embedding, torch.norm(V, dim=2)], dim=1)
        print(f"stack.shape", stack.shape)
        stack = self.linear_update1(stack)
        stack = F.silu(stack)
        split = self.linear_update2(stack)
        split1 = split[:, :self.num_embeddings]  # First part, contains the first 128 elements in the second dimension
        split2 = split[:, self.num_embeddings: 2*self.num_embeddings]  # Second part, contains the next 128 elements
        split3 = split[:, 2*self.num_embeddings:]  # Third part, contains the last 128 elements
        print(f"split1 size: ", split1.shape)
        print(f"split2 size: ", split2.shape)
        print(f"split3 size: ", split3.shape)
        split1_expanded = split1.unsqueeze(-1)
        equivariant_repr = torch.mul(U, split1_expanded)
        print(torch.sum(U * V, dim=2).shape)
        embedding = split2 + torch.sum(U * V, dim=2) \
                     * split3

        return equivariant_repr, embedding

    def forward(self, data):
        pos, z, neighbours = data.pos, data.z, data.neighbours

        # 1. Initialize inputs (s and v)
        embeddings = self.embeddings(z) # [batch_size, num_embeddings]
        equivariant_repr = torch.zeros((len(z), self.num_embeddings, 3))
        print(embeddings.shape)
        print('batch:', data.batch)

        # 2. Send messages and make updates
        for i in torch.arange(len(z)): # for every atom
            # get all atoms in the same molecule
            atoms_ids = torch.where(torch.tensor(data.batch) == data.batch[i])[0]
            atoms = data[atoms_ids]
            #print(atoms)
            # get neighbours of atom (ids) and their relative position
            neighbours_idx = neighbours[i].nonzero(as_tuple=True)[0] # [num_neighbours]
            rel_pos = pos[i] - pos

            print(f'embeddings[{i}]:', embeddings[i].shape)

            # send message (only to neighbours)
            delta_v, delta_s = self.message(equivariant_repr[neighbours_idx], embeddings[neighbours_idx], rel_pos[neighbours_idx])
            equivariant_repr[i] += delta_v
            embeddings[i] += delta_s

            #break

            # update
            # equivariant_repr[i], embeddings[i] += self.update(equivariant_repr[neighbours_idx], embeddings[neighbours_idx])

        # 3. Final linear layer
        output = 0
        return output

def create_dummy_data(num_neighbours, num_embeddings):
    # Create a dummy equivariant representation tensor
    equivariant_repr = torch.randn(num_neighbours, num_embeddings, 3)

    # Create a dummy embedding tensor
    embedding = torch.randn(num_neighbours, num_embeddings)

    return equivariant_repr, embedding

if __name__ == "__main__":
    # cutoff_dist = 5

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

    # net = PaiNN(9, 128, cutoff_dist)
    # net(next(iter(train_loader))
    num_neighbours = 5 # You can change this number to simulate different numbers of neighbours
    num_embeddings = 128

    #Create dummy data for dim testing
    #equivariant_repr, embedding = create_dummy_data(num_neighbours, num_embeddings)

    # Instantiate the PaiNN model
    model = PaiNN(num_atoms=9, num_embeddings=num_embeddings, cutoff_dist=5) # Adjust the parameters as needed

    # Test dims in update block
    # print(f"Equivariant size", equivariant_repr.shape)
    # print(f"Embeddig size", embedding.shape)
    # updated_equivariant_repr, updated_embedding = model.update(equivariant_repr, embedding)

    # Testing
    batch = next(iter(train_loader))
    print(batch)

    molecule = dataset[2]
    model(batch)

    # # Now you can check the dimensions and values of updated_equivariant_repr and updated_embedding
    # print("Updated Equivariant Representation Shape:", updated_equivariant_repr.shape)
    # print("Updated Embedding Shape:", updated_embedding.shape)
