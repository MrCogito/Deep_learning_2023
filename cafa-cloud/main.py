import sys
import os

import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.datasets import QM9
from torch_geometric.loader import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
import wandb

import train
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from PaiNN import PaiNN

def load_data(path, batch_size, train_size=0.8, val_size=0.1):
    ### load data
    dataset = QM9(root=path)

    # Calculate split lengths
    total_length = len(dataset)
    train_length = int(train_size * total_length)
    val_length = int(val_size * total_length)
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

    rootdir = "/home/mikk/Deep_learning_2023"
    resume_training = False
    resume_from = 250

    ### Hyperparameters
    param = 2 #0..15, see readme
    config = {
        "param": param,
        "name":  f"cafa-param-{param}-std",
        "batch_size": 100,
        "train_size": 0.8,
        "test_size":  0.1,

        "num_atoms":      10,
        "num_embeddings": 128,
        "cutoff_dist":    5,
        "hidden_out_dim": 128,

        "epochs":         500,
        "learning_rate":  5e-4,
        "weight_decay":   0.01,
        "smoothing_factor": 0.7,
        "device":           device
    }
    save_path = f"{rootdir}/models/{config['name']}"
    if not resume_training:
        if os.path.exists(save_path):
            print("Run with this name already exists!")
            exit()
            # pass
        else:
            os.mkdir(save_path)

    # stdout and stderr to a file
    sys.stdout = open(f"{save_path}/out.log", "a", buffering=1)
    sys.stderr = sys.stdout
    print(f"PID on cafa-cloud: {os.getpid()}")

    if resume_training:
        print(f"Resuming run {config['name']} from epoch {resume_from}")
        config_loaded = train.get_config(f"{save_path}/epoch_{resume_from}.pth")
        for k, v in config_loaded.items():
            config[k] = v
        print(config)

    train_loader, val_loader, test_loader = load_data(f"{rootdir}/data", config["batch_size"], config["train_size"], config["test_size"])
    print("Data loaded and split")

    ### Training
    # Instantiate the PaiNN model
    model = PaiNN(num_atoms=config["num_atoms"], num_embeddings=config["num_embeddings"],
                  cutoff_dist=config["cutoff_dist"], hidden_out_dim=config["hidden_out_dim"], device=device)
    model.to(device)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=config["learning_rate"], weight_decay=config["weight_decay"])
    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5, verbose=True)

    smoothed_val_loss = None
    from_epoch = 0
    if resume_training:
        model, optimizer, scheduler, from_epoch, smoothed_val_loss = train.get_state(f"{rootdir}/models/{config['name']}/epoch_{resume_from}.pth", model, optimizer, scheduler)

    config["criterion"] = criterion.__class__.__name__
    config["optimizer"] = optimizer.__class__.__name__
    config["scheduler"] = scheduler.__class__.__name__

    ### wandb setup
    wandb.login()
    if resume_training:
        if "wandbid" in config.keys():
            wandb.init(project="cafa", name=config["name"], resume='allow', id=config["wandbid"])
            print(f"Attached to wandb run with id {config['wandbid']}")
        else:
            print("Can't attach to any previous wandb runs")
            wandb.init(project="cafa", name=config["name"], resume=True)
    else:
        config["wandbid"] = wandb.util.generate_id()
        wandb.init(project="cafa", name=config["name"], config=config, id=config["wandbid"])

    print("Start training")
    train.training_loop(model, optimizer, criterion, scheduler, train_loader, val_loader, config, save_path,
                        from_epoch=from_epoch, smoothed_val_loss=smoothed_val_loss)