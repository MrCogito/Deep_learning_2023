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

    epochs_per_dataset: float = 0.1
    batch_size: int = 8192

    model_depth: int = 3
    neurons_per_layer: int = 128
    dropout: float = 0.2

    one_step_learning: bool = False
    lr: float = 2e-4
    weight_decay: float = 0
    max_bytes: int = 2 * 10**8
    # SETUP PARAMATERS
    def run(self, name: str, time: int, max_bytes: int, isServer: bool, data_folder_name: str, epochs_per_dataset: float, batch_size: int, model_depth: int, neurons_per_layer: int, dropout: float, one_step_learning: bool, lr: float, weight_decay: float):
        kv_start(name)
        start = seconds()

        folder = f"outputs/{'-'.join(name.split('-')[:-1])}/{name}/"
        if not exists(folder): mkdir(folder)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # SETUP WANDB
        if (isServer): wandb.init(project="Project_name", name=name, config={"epochs_per_dataset": epochs_per_dataset, "batch_size": batch_size, "model_depth": model_depth, "neurons_per_layer": neurons_per_layer, "dropout": dropout, "one_step_learning": one_step_learning, "lr": lr, "max_bytes": max_bytes, "data_folder_name": data_folder_name, "isServer": isServer, "device": str(device)})
        print(device)
        #ADD MODEL
        model = Net(dropout, model_depth, neurons_per_layer, lr, weight_decay).to(device) 
        #SETNPATH to folder on serwer
        if (isServer): path = "../../../../../../../work1/s183914/"
        else: path = ""
        data_path = path + 'dataset_processed/' + data_folder_name + "/"
        data_files = os.listdir(data_path)
        #this is probably to dell
        # shuffle data_files
        torch.manual_seed(0)
        data_files = [data_files[i] for i in torch.randperm(len(data_files))]
        data_files_train_unshuffled = data_files[:int(len(data_files) * 0.95)]
        data_files_test = data_files[int(len(data_files) * 0.95):]
        training_time, data_load_time = 0, 0
        for i in range(10000000):
            data_files_train = data_files_train_unshuffled.copy()
            torch.manual_seed(i)
            data_files_train = [data_files_train[i] for i in torch.randperm(len(data_files_train))]

            train_loss, test_loss, accuracy, train_batches, test_batches = 0, 0, 0, 0, 0
            data_train_iterator = data_loader(data_files_train, data_path, max_bytes, device)
            start_time_of_load = seconds()
            for train_batches, data_train in enumerate(data_train_iterator):
                data_load_time += seconds() - start_time_of_load
                data_x, data_y = model.prep_data(data_train)
                start_time_of_training = seconds()
                for _ in range(max(int(epochs_per_dataset), 1)):
                    idx = torch.randperm(data_x.shape[0])
                    data_x, data_y = data_x[idx], data_y[idx]
                    if epochs_per_dataset < 1:
                        data_x, data_y = data_x[:int(data_x.shape[0] * epochs_per_dataset)], data_y[:int(data_y.shape[0] * epochs_per_dataset)]
                    loss = model.trainer_simple(data_x, data_y, batch_size)
                    train_loss += loss / max(int(epochs_per_dataset), 1)
                    # print("Train Loss: " + str(round(loss, 5)), end="\r")
                training_time += seconds() - start_time_of_training
                start_time_of_load = seconds()
                # print_gpu_memory()
            print("time spent loading data: " + str(round(data_load_time, 5)), "time spent training: " + str(round(training_time, 5)))
            data_test_iterator = data_loader(data_files_test, data_path, max_bytes=2*10**9, device=device)
            for test_batches, data_test in enumerate(data_test_iterator):
                data_x, data_y = model.prep_data(data_test)
                loss, acc = model.evaluate(data_x, data_y, batch_size)
                test_loss += loss   
                accuracy += acc
            if (isServer): wandb.log({"Train Loss: ": train_loss / (train_batches + 1), "Test Loss: ": test_loss / (test_batches + 1), "Accuracy: ": accuracy / (test_batches + 1)})
            else: print("Train Loss: " + str(round(train_loss / (train_batches + 1), 5)), "Test Loss: " + str(round(test_loss / (test_batches + 1), 5)), "Accuracy: " + str(round(accuracy / (test_batches + 1), 5)))
            
            if not kv_is_running(name):
                print(f"Stopped: epoch {i}")
                break
            if seconds() - start > time:
                print(f"Time limit reached: epoch {i}")
                break
        model.save(folder + "model.pt")
        kv_stop(name)




Defaults.start()
