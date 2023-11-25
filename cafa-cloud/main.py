import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import torch
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
import wandb

from PaiNN import PaiNN


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

### load data
dataset = QM9(root=f"./data")

# Calculate split lengths
total_length = len(dataset)
train_length = int(0.8 * total_length)
val_length = int(0.1 * total_length)
test_length = total_length - train_length - val_length

# Perform random split
train_set, val_set, test_set = torch.utils.data.random_split(dataset,
                                                                [train_length, val_length, test_length],
                                                                generator=torch.Generator().manual_seed(42))

# Create data loaders
train_loader = DataLoader(train_set, batch_size=32)
val_loader = DataLoader(val_set, batch_size=32)
test_loader = DataLoader(test_set, batch_size=32)


### Testing
# Instantiate the PaiNN model
model = PaiNN(num_atoms=9, num_embeddings=128, cutoff_dist=5, hidden_out_dim=128, device=device) # Adjust the parameters as needed
model.to(device)
batch = next(iter(train_loader))
batch.to(device)
print(device)
print(batch)

out = model(batch)
print(out.shape)