import torch
from __future__ import annotations
from dtu import Parameters, dtu, GPU
import os
from os import mkdir
from os.path import exists
from time import time as seconds





@dtu
class Defaults(Parameters):
    name: str = "experiment-name"
    instances: int = 1
    GPU: None | GPU = GPU.v32
    time: int = 84600 # 23.5 hours
    data_folder_name: str = "todo"

    # SETUP PARAMATERS
    def run(self, name: str, time: int, max_bytes: int, isServer: bool, data_folder_name: str, epochs_per_dataset: float, batch_size: int, model_depth: int, neurons_per_layer: int, dropout: float, one_step_learning: bool, lr: float, weight_decay: float):

        start = seconds()

        folder = f"outputs/{'-'.join(name.split('-')[:-1])}/{name}/"
        if not exists(folder): mkdir(folder)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # SETUP WANDB
        #if (isServer): wandb.init(project="Project_name", name=name, config={ "neurons_per_layer": neurons_per_layer, "dropout": dropout, "one_step_learning": one_step_learning, "lr": lr, "max_bytes": max_bytes, "data_folder_name": data_folder_name, "isServer": isServer, "device": str(device)})
        print(device)
        #ADD MODEL
        
        


        #SETNPATH to folder on serwer
        if (isServer): path = "../../../../../../../work1/s183914/"
        else: path = ""





Defaults.start()
