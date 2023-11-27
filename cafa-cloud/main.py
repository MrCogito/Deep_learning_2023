import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
import wandb

from PaiNN import PaiNN
from train import training_loop

### Hyperparameters
name = "cafa-param-01-vol2"
save_path = f"/home/mikk/Deep_learning_2023/models/{name}"
param          = 1
epochs         = 500
batch_size     = 64
num_atoms      = 10
num_embeddings = 128
cutoff_dist    = 5
hidden_out_dim = 128
learning_rate  = 0.001
weight_decay   = 0.01

def load_data(path, batch_size):
    ### load data
    dataset = QM9(root=path)

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
    train_loader = DataLoader(train_set, batch_size=batch_size)
    val_loader = DataLoader(val_set, batch_size=batch_size)
    test_loader = DataLoader(test_set, batch_size=batch_size)
    return train_loader, val_loader, test_loader

if __name__ == "__main__":
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    train_loader, val_loader, test_loader = load_data("/home/mikk/Deep_learning_2023/data", batch_size)
    print("Data loaded and split")

    ### Training
    # Instantiate the PaiNN model
    model = PaiNN(num_atoms=num_atoms, num_embeddings=num_embeddings, cutoff_dist=cutoff_dist, hidden_out_dim=hidden_out_dim, device=device) # Adjust the parameters as needed
    model.to(device)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)

    ### wandb setup
    wandb.login()
    wandb.init(project="PaiNN", name=name, config={
        "param": param,
        "epochs": epochs,
        "batch_size": batch_size,
        "num_atoms": num_atoms,
        "num_embeddings": num_embeddings,
        "cutoff_disc": cutoff_dist,
        "criterion": criterion.__class__.__name__,
        "Optimizer": optimizer.__class__.__name__,
        "Learning_rate": learning_rate,
        "weight_decay": weight_decay,
        "device": str(device)
    })

    print("Start training")
    training_loop(model, train_loader, val_loader, epochs, optimizer, criterion, param, device, save_path)