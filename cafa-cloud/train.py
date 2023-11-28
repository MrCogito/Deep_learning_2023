import torch
import wandb
import torch.nn.functional as F

def get_config(file):
    saved_state = torch.load(file)
    config = saved_state["config"]
    return config

def get_state(file, model, optimizer, scheduler):
    saved_state = torch.load(file)
    from_epoch = saved_state["epoch"]
    model.load_state_dict(saved_state["model"])
    optimizer.load_state_dict(saved_state["optimizer"])
    scheduler.load_state_dict(saved_state["scheduler"])
    smoothed_val_loss = saved_state["smoothed_val_loss"]
    return model, optimizer, scheduler, from_epoch, smoothed_val_loss

def training_loop(model, optimizer, criterion, scheduler, train_loader, val_loader, config, save_path, logger, from_epoch=0, smoothed_val_loss=None):
    epochs = config["epochs"]
    device = torch.device(config["device"])
    param = config["param"]
    smoothing_factor = config["smoothing_factor"]

    for epoch in range(from_epoch, epochs):
        model.train()
        total_train_loss, total_train_mae = 0.0, 0.0


        for batch in train_loader:
            batch.to(device)
            optimizer.zero_grad()
            #Forward pass
            output = model(batch)
            # Assuming 'output' and 'batch.y' are aligned for loss calculation
            loss = criterion(output.squeeze(), batch.y[:, param])
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()
            total_train_mae += F.l1_loss(output.squeeze(), batch.y[:, param], reduction='sum').item()



        avg_train_loss = total_train_loss / len(train_loader.dataset)
        avg_train_mae = total_train_mae / len(train_loader.dataset)

        logger.info(f'Epoch [{epoch+1}/{epochs}], Train Loss: {avg_train_loss:.4f}, Train L1 Loss: {avg_train_mae:.4f}' )


        # Validation phase
        model.eval()
        total_val_loss, total_val_mae = 0.0, 0.0


        with torch.no_grad():
            for batch in val_loader:
                batch.to(device)
                output = model(batch)
                loss = criterion(output.squeeze(), batch.y[:, param])
                total_val_loss += loss.item()
                total_val_mae += F.l1_loss(output.squeeze(), batch.y[:, param], reduction='sum').item()



        avg_val_loss = total_val_loss / len(val_loader.dataset)
        avg_val_mae = total_val_mae / len(val_loader.dataset)
        # Apply exponential smoothing to validation loss
        if smoothed_val_loss is None:
            smoothed_val_loss = avg_val_loss
        else:
            smoothed_val_loss = (smoothing_factor * smoothed_val_loss) + ((1 - smoothing_factor) * avg_val_loss)

        logger.info(f'Epoch [{epoch+1}/{epochs}], Validation Loss: {avg_val_loss:.4f}, Validation L1: {avg_val_mae:.4f}, Smoothed Validation Loss: {smoothed_val_loss:.4f}')

        # Adjust learning rate based on smoothed validation loss
        scheduler.step(smoothed_val_loss)

        wandb.log({"train_loss": avg_train_loss, "train l1 loss": avg_train_mae, "val loss": avg_val_loss, "val l1 loss": avg_val_mae, "smoothed val loss":smoothed_val_loss })
        if (epoch + 1) % 5 == 0:
            # Save the model
            save_dict = {
                "epoch": epoch,
                "config": config,
                "model": model.state_dict(),
                "smoothed_val_loss": smoothed_val_loss,
                "scheduler": scheduler.state_dict(),
                "optimizer": optimizer.state_dict()
            }
            torch.save(save_dict, f"{save_path}/epoch_{epoch+1}.pth")

    save_dict = {
        "epoch": epoch,
        "config": config,
        "model": model.state_dict(),
        "smoothed_val_loss": smoothed_val_loss,
        "scheduler": scheduler.state_dict(),
        "optimizer": optimizer.state_dict()
    }
    torch.save(save_dict, f"{save_path}/final.pth")
    wandb.finish()
