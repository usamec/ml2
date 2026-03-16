import argparse
import json

import numpy as np
import torch
from sklearn.metrics import roc_auc_score
from tqdm import tqdm

from model import create_model


def evaluate(checkpoint_path: str, data_path: str) -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # ------------------------------------------------------------------
    # Load model
    # ------------------------------------------------------------------
    model = create_model().to(device)
    state_dict = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(state_dict)
    model.eval()
    print(f"Loaded checkpoint from '{checkpoint_path}', total parameters {sum(p.numel() for p in model.parameters())}")

    # ------------------------------------------------------------------
    # Load data
    # ------------------------------------------------------------------
    with open(data_path, "r") as f:
        dataset = json.load(f)
    print(f"Loaded {len(dataset)} sequences from '{data_path}'\n")

    # ------------------------------------------------------------------
    # Evaluate sequence by sequence
    # ------------------------------------------------------------------
    all_probs = []
    all_labels = []

    with torch.no_grad():
        for i, item in enumerate(tqdm(dataset, desc="Evaluating")):
            sequence = item["sequence"]
            label = item["label"]

            x = torch.tensor(sequence, dtype=torch.float32).unsqueeze(0).to(device)  # (1, L)
            logit = model(x).squeeze().item()  # scalar logit
            prob = 1.0 / (1.0 + np.exp(-logit))  # sigmoid -> probability

            all_probs.append(prob)
            all_labels.append(label)

    # ------------------------------------------------------------------
    # Summary metrics
    # ------------------------------------------------------------------
    all_probs_np = np.array(all_probs)
    all_labels_np = np.array(all_labels)
    preds = (all_probs_np >= 0.5).astype(int)

    accuracy = (preds == all_labels_np).mean()

    try:
        auc = roc_auc_score(all_labels_np, all_probs_np)
    except ValueError:
        auc = float("nan")

    print("\n" + "=" * 50)
    print(f"Total sequences : {len(dataset)}")
    print(f"Accuracy        : {accuracy:.4f}")
    print(f"AUC             : {auc:.4f}")
    print("=" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a trained model on a JSON sequence dataset.")
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="model.pth",
        help="Path to the model checkpoint file (default: model.pth)",
    )
    parser.add_argument(
        "--data",
        type=str,
        default="eval_easy.json",
        help="Path to the JSON data file produced by generate_easy.py (default: eval_easy.json)",
    )
    args = parser.parse_args()

    evaluate(checkpoint_path=args.checkpoint, data_path=args.data)
