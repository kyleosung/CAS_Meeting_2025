import torch
import torch.nn as nn
import torch.nn.functional as F

torch.set_default_dtype(torch.float64)


class Net(nn.Module):
    def __init__(self, input_dim: int = 11, output_dim: int = 1) -> None:
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_dim, 150)
        self.fc2 = nn.Linear(150, 300)
        self.fc3 = nn.Linear(300, output_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
