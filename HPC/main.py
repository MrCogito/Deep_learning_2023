from __future__ import annotations
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import torch
from dtu import Parameters, dtu, GPU
from os import mkdir
from os.path import exists
from time import time as seconds
import torch.nn as nn
import torch.optim as optim
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from train import training_loop
from PaiNN import PaiNN
import wandb

@dtu
class Defaults(Parameters):
    name: str = "experiment-name"
    instances: int = 1
    GPU: None | GPU = GPU.v32
    time: int = 84600 # 23.5 hours
    #data_folder_name: str = "data_fod"
    epochs: int = 1000
    batch_size: int = 32  
    isServer: bool = True

    num_atoms: int =10
    num_embeddings: int =128
    cutoff_dist: float=5
    hidden_out_dim: int =128
    # SETUP PARAMATERS
    def run(self, name: str, time: int, isServer: bool, epochs: int, batch_size: int, num_atoms: int, num_embeddings: int, cutoff_dist: float, hidden_out_dim: int):

        start = seconds()
        
        folder = f"outputs/{'-'.join(name.split('-')[:-1])}/{name}/"
        if not exists(folder): mkdir(folder)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        param = 1
        
        # load and prep dataset
        dataset = QM9(root=f"./data")
        total_length = len(dataset)
        train_length = int(0.8 * total_length)
        val_length = int(0.1 * total_length)
        test_length = total_length - train_length - val_length

        model = PaiNN(num_atoms=num_atoms, num_embeddings=num_embeddings, cutoff_dist=cutoff_dist, hidden_out_dim=hidden_out_dim).to(device)
        # Perform random split
        criterion = nn.MSELoss() 
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        train_set, val_set, test_set = torch.utils.data.random_split(dataset,
                                                                        [train_length, val_length, test_length],
                                                                        generator=torch.Generator().manual_seed(42))

        # Create data loaders
        train_loader = DataLoader(train_set, batch_size)
        val_loader = DataLoader(val_set, batch_size)
        test_loader = DataLoader(test_set, batch_size)

        wandb.init(project="deeplearning_painn", name=name, config={
            "epochs": epochs,
            "batch_size": batch_size,
            "num_atoms": num_atoms,
            "num_embeddings": num_embeddings,
            "cutoff_disc": cutoff_dist,
            "criterion": criterion.__class__.__name__,
            "Optimizer": optimizer.__class__.__name__,
            "device": str(device),
            "Learning_rate": 0.001,
        })

        training_loop(model=model, train_loader=train_loader, val_loader=val_loader, epochs=epochs, optimizer=optimizer, criterion=criterion, param=param, isServer=isServer, name=name, batch_size=batch_size, num_atoms=num_atoms, num_embeddings=num_embeddings, cutoff_dist=cutoff_dist, device=device)

        print(device)
        #ADD MODEL

        #SETNPATH to folder on serwer
        #if (isServer): path = "../../../../../../../work1/s183914/"
        #else: path = ""
        





Defaults.start()
