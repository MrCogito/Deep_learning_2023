import torch

def remove_key_prefix(state_dict, key_prefix="_orig_mod."):
    new_state_dict = {}
    for key, value in state_dict.items():
        # Key remapping: "_orig_mod." prefix removed
        new_key = key.replace(key_prefix, "")
        new_state_dict[new_key] = value
    return new_state_dict

def load_model(model, path, device="cpu"):
    state_dict = torch.load(path, map_location=torch.device(device))
    state_dict = remove_key_prefix(state_dict) # remapping keys - the saved models had "_orig_mod." as a prefix which I remove here
    model.load_state_dict(state_dict)
    return model

def test(model, test_loader, param, device="cpu"):
    with torch.no_grad():
        model.eval()  # Set the model in evaluation mode
        criterion = torch.nn.L1Loss() # Mean Absolute Error (MAE)
        total_loss = 0.0
        total_samples = 0

        counter = 1
        batch_count = len(test_loader)
        for batch in test_loader:
            batch.to(device)
            batch_size = len(batch)
            targets = batch.y[:, param]
            predictions = model(batch)

            #print(f'{predictions[0]} vs {targets[0]}')

            # Calculate loss (MAE) for this batch
            loss = criterion(predictions.squeeze(), targets)

            # Update total loss
            total_loss += loss.item() * batch_size
            total_samples += batch_size

            # print
            print(f'Batch {counter}/{batch_count} Loss:', loss.item())
            counter += 1

        # Calculate average MAE for entire test set
        avg_loss = total_loss / total_samples

    return avg_loss


if __name__ == "__main__":
    from PaiNN import PaiNN
    # Model parameters
    num_atoms: int =10
    num_embeddings: int =128
    cutoff_dist: float=5
    hidden_out_dim: int =128
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model_arch = PaiNN(num_atoms=num_atoms, num_embeddings=num_embeddings, cutoff_dist=cutoff_dist, hidden_out_dim=hidden_out_dim, device=device).to(device)

    # Load model
    model = load_model(
        model_arch, # original model architecture
        "models_hpc/12fixWorkingSetup-0/epoch_230.pth", # these are the saved final weights in the trained model
        device)
    
    # test on data
    from torch_geometric.datasets import QM9
    from torch_geometric.loader import DataLoader

    batch_size: int = 80

    dataset = QM9(root=f"./data")
    total_length = len(dataset)
    train_length = int(0.8 * total_length)
    val_length = int(0.1 * total_length)
    test_length = total_length - train_length - val_length

    train_set, val_set, test_set = torch.utils.data.random_split(dataset,
                                                                 [train_length, val_length, test_length],
                                                                 generator=torch.Generator().manual_seed(42))
    test_loader = DataLoader(test_set, batch_size)

    parameter = 12
    average_loss = test(model, test_loader, param=parameter)

    print(f'Average loss for param={parameter}:', average_loss)