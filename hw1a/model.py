import torch
import torch.nn as nn

class LambdaLayer(nn.Module):
    def __init__(self, func):
        super().__init__()
        self.func = func
    
    def forward(self, x):
        return self.func(x)

def create_model():
    # No sigmoid at the end, evaluation handles this by itself
    return nn.Sequential(
        LambdaLayer(lambda x: x.unsqueeze(1)),
        nn.Conv1d(1, 16, 20, stride=20),
        nn.ReLU(),
        nn.Conv1d(16, 16, 15, padding=7),
        nn.AdaptiveAvgPool1d(1),
        LambdaLayer(lambda x: x.view(x.size(0), -1)),
        nn.Linear(16, 1)
    )