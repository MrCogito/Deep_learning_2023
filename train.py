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


epochs = 10
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


def training_loop(model):
    running_loss = 0.0
    for epoch in range(epochs):
        model.train()
        # Zero the gradients
        optimizer.zero_grad()

        batch = next(iter(train_loader))

        # Forward pass
        output = model(batch)

        # Calculate the loss
        loss = criterion(output)

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        # Print statistics
        running_loss += loss.item()
        print(running_loss)


training_loop(model)

