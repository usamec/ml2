# Homework variant B

## General description

We will do a quantized linear regression.
You are given inputs $X$ and target outputs $Y$, your goal is to find a weight $W$ such that $||XW - Y||_2$ is minimal and individual weights from $W$ are from {-3, -2, -1, 0, 1, 2, 3}.

## Data and setup

Data are in data.pt file (check eval.py and solve.py on how to load it).
Evaluation (and checking whether weights are correct) is done by the eval.py script.
Example dummy solution is in solve.py.

## First task (30%)

Find $W$ using (stochastic) gradient descent and straight-through estimator, i.e., you will look for contiguous $W'$, which you then quantize to $W = q(W')$ and compute loss and gradient. We pretend that the derivative of q is one everywhere. Use a constant learning rate.
You should get a mean squared error of at most 14 (but with a little luck, you can get less than 12).

## Second task (40%)

Use linearly decaying learning rate (i.e. $\eta(t) = \eta_0 (1 - \frac{t}{T})$, where $\eta_0$ is initial learning rate and $T$ is number of iterations and $t$ is the current iteration).
Run optimization for a long time (if you get a reasonable solution, try doubling the optimization steps).
If done right, you should MSE around 9.
Track loss after each step and plot it. Does it look reasonable?
What is happening with continuous weights $W'$ during optimization, and what with quantized weights $W$? This should not have a one-sentence answer, but rather multiple pages.

## Third task (30%)

Based on previous observations, do something better (I can do slightly less than 7 MSE).

## What to submit

Training code for each subtask, weights for each subtask, and a PDF report (mainly focusing on the second task and explaining your techniques in the third task).

## Allowed and disallowed techniques

You can use AI as you wish, but describe how you use it and keep in mind that you must understand everything inside your solution.
Also, if you want to use autoresearch by Andrej Karpathy, knock yourself out.

