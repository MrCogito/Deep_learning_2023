import torch
import torch.nn as nn
import torch.optim as optim
from PaiNN import PaiNN
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch_geometric.utils import scatter
from torch.optim.lr_scheduler import ReduceLROnPlateau
import wandb

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
model = PaiNN(num_atoms=10, num_embeddings=128, cutoff_dist=5, hidden_out_dim=128) # Adjust the parameters as needed


epochs = 32 
criterion = nn.MSELoss() 
optimizer = optim.Adam(model.parameters(), lr=0.001)


def training_loop(model, train_loader, val_loader, epochs, optimizer, criterion, param, isServer, name, batch_size, num_atoms, num_embeddings, cutoff_dist, device ):

    #SETUP WANDB
    # SETUP WANDB
    if (isServer): 
        wandb.init(project="deeplearning_painn", name=name, config={ "epochs": epochs, "batch_size": batch_size, "num_atoms": num_atoms, "num_embeddings": num_embeddings, "cutoff_disc": cutoff_dist, "criterion": "MSELoss", "Optimizer": "Adam0001", "device": str(device)})

    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5, verbose=True)
    # Variable to keep track of smoothed validation loss
    smoothed_val_loss = None
    smoothing_factor = 0.9

    for epoch in range(epochs):
        model.train()
        total_train_loss = 0.0
        for batch in train_loader:
            optimizer.zero_grad()
            #Forward pass
            output = model(batch)
            # Assuming 'output' and 'batch.y' are aligned for loss calculation
            loss = criterion(output.squeeze(), batch.y[:, param])
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()
        avg_train_loss = total_train_loss / len(train_loader)
        print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {avg_train_loss:.4f}')

        # Validation phase
        model.eval()
        total_val_loss = 0.0
        with torch.no_grad():
            for batch in val_loader:
                output = model(batch)
                loss = criterion(output.squeeze(), batch.y[:, param])
                total_val_loss += loss.item()

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

    wandb.finish()
    torch.save(model.state_dict(), f"/path/to/myfolder/{name}.pth")


#training_loop(model, train_loader, val_loader, epochs, optimizer, criterion, 1)

