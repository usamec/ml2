import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import roc_auc_score

from model import create_model
from generator import generate_regular_sequence, generate_irregular_sequence


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class SequenceDataset(Dataset):
    """Generates sequences on-the-fly.

    label 0 -> regular sequence
    label 1 -> irregular sequence
    """

    def __init__(self, size: int = 10000, seq_length: int = 1000):
        self.size = size
        self.seq_length = seq_length

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        if idx % 2 == 0:
            seq = generate_regular_sequence(self.seq_length)
            label = 0
        else:
            seq = generate_irregular_sequence(self.seq_length)
            label = 1

        x = torch.tensor(seq, dtype=torch.float32)
        y = torch.tensor(label, dtype=torch.float32)
        return x, y


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train(
    num_epochs: int = 5,
    batch_size: int = 32,
    lr: float = 1e-3,
    dataset_size: int = 10000,
    seq_length: int = 1000,
    report_last_k: int = 10,
):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Data
    dataset = SequenceDataset(size=dataset_size, seq_length=seq_length)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    # Model
    model = create_model().to(device)

    # Optimizer & loss
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = nn.BCEWithLogitsLoss()

    for epoch in range(1, num_epochs + 1):
        model.train()

        losses = []
        logits = []
        labels = []


        for batch_idx, (x, y) in enumerate(loader):
            x, y = x.to(device), y.to(device)

            optimizer.zero_grad()
            model_out = model(x).squeeze(1)        # (B,)
            loss = criterion(model_out, y)
            loss.backward()
            optimizer.step()

            losses.append(loss.item())
            logits.append(model_out.detach().cpu())
            labels.append(y.detach().cpu())

        # ---------- Reporting ----------
        avg_loss = float(np.mean(losses))

        all_logits = torch.cat(logits).numpy()
        all_labels = torch.cat(labels).numpy()
        # Convert logits -> probabilities for AUC
        all_probs = 1.0 / (1.0 + np.exp(-all_logits))   # sigmoid

        try:
            auc = roc_auc_score(all_labels, all_probs)
        except ValueError:
            auc = float("nan")   # edge case: only one class in window

        print(
            f"Epoch {epoch}/{num_epochs} | "
            f"avg loss: {avg_loss:.4f} | "
            f"AUC: {auc:.4f}"
        )

    print("Training complete.")
    torch.save(model.state_dict(), "model.pth")


if __name__ == "__main__":
    train()
