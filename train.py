import torch
import torch.nn as nn
import torch.optim as optim
from PaiNN import PaiNN
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch_geometric.utils import scatter

### load data
dataset = QM9(root=f"./data/{5}A")

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
model = PaiNN(num_atoms=9, num_embeddings=128, cutoff_dist=5, hidden_out_dim=128) # Adjust the parameters as needed


epochs = 1
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


def training_loop(model, train_loader, val_loader, epochs, optimizer, criterion):

    for epoch in range(epochs):
        model.train()
        total_train_loss = 0.0
        for batch in train_loader:
            optimizer.zero_grad()
            #Forward pass
            output = model(batch)
            # Assuming 'output' and 'batch.y' are aligned for loss calculation
            loss = criterion(output, batch.y) 
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
                loss = criterion(output, batch.y)
                total_val_loss += loss.item()

        avg_val_loss = total_val_loss / len(val_loader)
        print(f'Epoch [{epoch+1}/{epochs}], Validation Loss: {avg_val_loss:.4f}')



training_loop(model, train_loader, val_loader, epochs, optimizer, criterion)

