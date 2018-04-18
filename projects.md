# Final projects suggestions (work in progress)

### Conditional computation

Take a paper about conditional computation (TODO) and do following things:

* Take a simple dataset (like MNIST or CIFAR-10, ...)
* Train some simple nonconditional model M1
* Train conditional model M2 with similar computational cost (prediction time) as M1

The goal is to have much better accuracy of M2 model than M1. Also they should be quite similar in other architecture considerations (like both should be convnets, or fully connected nets, ...).

### Sparsification

Apply sparsification techniques from some paper (TODO) and demostrate that it can lead into faster models with comparable accuracy.

### Bayesian neural nets

Take a very simple dataset (simpler than MNIST). Use PyMC3 to estimate distribution of neural network parameters.
Demostrate, than this distrubution gives you something useful (TODO ideas).
