import torch

X, Y = torch.load("data.pt")

W = (torch.rand((256, 128)) * 6 - 3).round()

torch.save(W, "solution.pt")