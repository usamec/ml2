# Homework variant B

## General description

We will do a quantized linear regression.
You are given inputs $X$ and target outputs $Y$, your goal is to find weight $W$ such that $||XW - Y||_2$ is minimal and individual weights from $W$ are from ${-3, -2, -1, 0, 1, 2, 3}$.

## Data and setup

Data are in data.pt file (check eval.py and solve.py how to load it).
Evaluation (and checking whether weights are correct) is done by eval.py script.
Example dummy solution is in solve.py.

## First task (30%)

Find $W$ using (stochastic) gradient descent and straight-through estimator, i.e. you will look for contigous $W'$, which you then quantized to $W = q(W')$ and compute loss and gradient. We pretend that derivative of q is one everywhere. Use a constant learning rate.
You should get mean squared error at most 14 (but will a little luck you can get less than 12).

## Second task (40%)

Use linearly decaying learning rate (i.e. $\eta(t) = \eta_0 (1 - \frac{t}{T})$, where $\eta_0$ is initial learning rate and $T$ is number of iterations and $t$ is the current iteration).
Run optimization for long time (if you get reasonable solution, try doubling the optimization steps).
If done right, you should get loss around 9.
Track loss after each step and plot it. Does it look reasonable?
What is happening with continuous weights $W'$ during optimization and what with quantized weights W? This should not have one sentence answer, but rather multiple pages.

## Third task (30%)

Based on previous observation do something better (I can do slightly less than 7 MSE).


