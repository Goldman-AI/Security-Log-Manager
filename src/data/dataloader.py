import torch
from torch.utils.data import Dataset, DataLoader

class SecurityLogsDataset(Dataset):
    def __init__(self, logs):
        self.logs = logs

    def __len__(self):
        return len(self.logs)

    def __getitem__(self, idx):
        return self.logs[idx]

# Example usage:
# logs = [....] # Load your security log data here
# dataset = SecurityLogsDataset(logs)
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
