from main import load_data
from train import get_config, get_state

import torch
import torch.nn as nn
from torch.optim.lr_scheduler import ReduceLROnPlateau
import torch.optim as optim
import torch.nn.functional as F

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from PaiNN import PaiNN

name = "cafa-param-14-vol4"
epoch = 130
dir = f"/home/mikk/Deep_learning_2023/models/{name}"

config = get_config(f"{dir}/epoch_{epoch}.pth")

train_loader, val_loader, test_loader = load_data("/home/mikk/Deep_learning_2023/data", config["batch_size"], config["train_size"], config["test_size"])
print("Data loaded")

model = PaiNN(num_atoms=config["num_atoms"], num_embeddings=config["num_embeddings"],
                  cutoff_dist=config["cutoff_dist"], hidden_out_dim=config["hidden_out_dim"], device='cpu')
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=config["learning_rate"], weight_decay=config["weight_decay"])
scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5, verbose=True)

model, optimizer, scheduler, from_epoch, smoothed_val_loss = get_state(f"{dir}/epoch_{epoch}.pth", model, optimizer, scheduler)

mean = -77.00674438476562
std = 10.49488639831543
total_mae = 0
for i, batch in enumerate(test_loader):
    output = model(batch)
    print(f"Batch {i}/{len(test_loader)}")
    total_mae += F.l1_loss(1000*output.squeeze(), 1000*(batch.y[:, config["param"]]-mean)/std).item()

mae = total_mae / len(test_loader)

print(f"MAE loss: {mae}")
