import torch
from torch_geometric.datasets import QM9
from torch_geometric.data import Data

k = 0
def add_neighbours(data: Data, cutoff=5.0, padto=30) -> Data:
    global k
    print(f"Molecule {k}")
    k += 1

    natoms = data.pos.shape[0]

    # i-th row is for i-th atom in data.z, ij element is distance between i-th and j-th atom
    distances = torch.cdist(data.pos, data.pos, p=2)

    # select atoms
    neighbours = torch.where(distances <= cutoff, 1, 0)

    # exclude itself
    neighbours = neighbours - torch.eye(natoms)

    # pad with zeros to have matching dimensions, otherwise pyg complains and won't save the data
    neighbours = torch.cat((neighbours, torch.zeros((natoms, padto-natoms))), dim=1)

    data.neighbours = neighbours
    return data

data = QM9(root="./data/5A", pre_transform=add_neighbours)



# max number of atoms -- 29
y = torch.cat([data[i].z for i in range(130831)])
print(torch.unique(y))
