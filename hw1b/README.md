# Homework variant B

## General description

We will do a quantized linear regression.
You are given inputs $X$ and target outputs $Y$, your goal is to find weight $W$ such that $||XW - Y||_2$ is minimal and individual weights from $W$ are from ${-3, -2, -1, 0, 1, 2, 3}$.

## Data and setup

Data are in data.pt file (check eval.py and solve.py how to load it).
Evaluation (and checking whether weights are correct) is done by eval.py script.
Example dummy solution is in solve.py.

## First task (30%)

Find $W$ using gradient descent and straight-through estimator, i.e. you will look for contigous $W'$, which you then quantized to $W = q(W')$ and compute loss and gradient. We pretend that derivative of q is one everywhere.
You should get squared error at most TODO.

## Second task (40%)

Look at change of $W'$ and $W$ between iteration later in the training. What is going on?

## Third task (30%)

Based on previous observation do something better.


