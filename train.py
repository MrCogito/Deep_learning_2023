import torch
import torch.nn as nn
import torch.optim as optim
from PaiNN import PaiNN
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch_geometric.utils import scatter


dataset = QM9(root=f"./data/{5}A")

train, validation, test = torch.utils.data.random_split(dataset, [0.8, 0.1, 0.1], generator=torch.Generator().manual_seed(42))

train_loader = DataLoader(train, batch_size=32)

epochs = 1
num_neighbours = 5 # You can change this number to simulate different numbers of neighbours
num_embeddings = 128

model = PaiNN(num_atoms=9, num_embeddings=num_embeddings, cutoff_dist=5) # Adjust the parameters as needed

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


def training_loop(model):
    running_loss = 0.0
    for epoch in range(epochs):
        model.train()
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        output = model(next(iter(train_loader)))

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

