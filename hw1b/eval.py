import torch
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Evaluate quantized linear regression solution.")
    parser.add_argument("--data", type=str, default="data.pt", help="Path to the data file (data.pt)")
    parser.add_argument("--solution", type=str, default="solution.pt", help="Path to the solution file (solution.pt)")
    args = parser.parse_args()

    # Load data
    try:
        X, Y = torch.load(args.data, weights_only=True)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

    # Load solution
    try:
        W = torch.load(args.solution, weights_only=True)
    except Exception as e:
        print(f"Error loading solution: {e}")
        sys.exit(1)

    # Check weights
    # 1. Shape check
    expected_shape = (X.shape[1], Y.shape[1])
    if W.shape != expected_shape:
        print(f"Error: Solution weight matrix has shape {W.shape}, but expected {expected_shape}.")
        sys.exit(1)

    # 2. Integer check
    is_integer = torch.all(W == W.round())
    if not is_integer:
        print("Error: Not all weights are integers.")
    else:
        # 3. Range check
        in_range = torch.all((W >= -3) & (W <= 3))
        if not in_range:
            print("Error: Weights are not in range [-3, 3].")
        else:
            print("All weights are correct (integers between -3 and 3).")

    # Calculate errors
    def calculate_mse(X, W, Y):
        return torch.mean((X @ W - Y)**2).item()

    sol_error = calculate_mse(X, W, Y)
    zero_error = calculate_mse(X, torch.zeros_like(W), Y)

    print(f"Solution error (MSE): {sol_error:.6f}")
    print(f"Zeros matrix error (MSE): {zero_error:.6f}")

if __name__ == "__main__":
    main()
