import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
import wandb

from PaiNN import PaiNN


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

### load data
dataset = QM9(root=f"/home/mikk/Deep_learning_2023/data")
save_path = "/home/mikk/Deep_learning_2023/models/cafa01"
name = "cafa01"

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
print("Data loaded and split")

### Hyperparameters
param          = 1
epochs         = 1
batch_size     = 32
num_atoms      = 10
num_embeddings = 128
cutoff_dist    = 5
hidden_out_dim = 128

### wandb setup
wandb.login()
wandb.init(project="PaiNN", name="cafa", config={
    "param": param,
    "epochs": epochs,
    "batch_size": batch_size,
    "num_atoms": num_atoms,
    "num_embeddings": num_embeddings,
    "cutoff_disc": cutoff_dist,
    "criterion": "MSELoss",
    "Optimizer": "Adam0001",
    "device": str(device)
})

def root_mean_squared_error(preds, targets):
    return torch.sqrt(torch.mean((preds - targets) ** 2))

### Training
# Instantiate the PaiNN model
model = PaiNN(num_atoms=10, num_embeddings=128, cutoff_dist=5, hidden_out_dim=128, device=device) # Adjust the parameters as needed
model.to(device)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


print("Start training")

scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5, verbose=True)
# Variable to keep track of smoothed validation loss
smoothed_val_loss = None
smoothing_factor = 0.9

for epoch in range(epochs):
    model.train()
    total_train_loss = 0.0
    total_train_rmse = 0.0

    for batch in train_loader:
        batch.to(device)
        optimizer.zero_grad()
        #Forward pass
        output = model(batch)
        # Assuming 'output' and 'batch.y' are aligned for loss calculation
        loss = criterion(output.squeeze(), batch.y[:, param])
        loss.backward()
        optimizer.step()
        print(batch)
        print(output.squeeze())
        total_train_loss += loss.item()
        total_train_rmse += root_mean_squared_error(output.squeeze(), batch.y[:, param])

    avg_train_loss = total_train_loss / len(train_loader)
    print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {avg_train_loss:.4f}')

    # Validation phase
    model.eval()
    total_val_loss = 0.0
    total_val_rmse = 0.0

    with torch.no_grad():
        for batch in val_loader:
            batch.to(device)
            output = model(batch)
            loss = criterion(output.squeeze(), batch.y[:, param])
            total_val_loss += loss.item()
            total_val_rmse += root_mean_squared_error(output.squeeze(), batch.y[:, param])


    avg_val_loss = total_val_loss / len(val_loader)
    # Apply exponential smoothing to validation loss
    if smoothed_val_loss is None:
        smoothed_val_loss = avg_val_loss
    else:
        smoothed_val_loss = (smoothing_factor * smoothed_val_loss) + ((1 - smoothing_factor) * avg_val_loss)

    print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {avg_train_loss:.4f}, Smoothed Validation Loss: {smoothed_val_loss:.4f}')

    # Adjust learning rate based on smoothed validation loss
    scheduler.step(smoothed_val_loss)

    wandb.log({"train_loss": avg_train_loss, "val loss": avg_train_loss, "smoothed val loss":smoothed_val_loss })
    if (epoch + 1) % 10 == 0:
        # Save the model
        torch.save(model.state_dict(), f"{save_path}/{name}_epoch_{epoch+1}.pth")

torch.save(model.state_dict(), f"{save_path}/{name}_final.pth")
wandb.finish()