# Final projects suggestions (work in progress)

### Conditional computation

Take a paper about conditional computation (https://arxiv.org/pdf/1701.06538.pdf, https://arxiv.org/pdf/1511.06297.pdf, https://arxiv.org/pdf/1308.3432.pdf, https://arxiv.org/pdf/1611.01144.pdf) and do following things:

* Take a simple dataset (like MNIST or CIFAR-10, ...)
* Train some simple nonconditional model M1
* Train conditional model M2 with similar computational cost (prediction time) as M1

The goal is to have much better accuracy of M2 model than M1. Also they should be quite similar in other architecture considerations (like both should be convnets, or fully connected nets, ...).

### Sparsification

Apply sparsification techniques from some paper (https://arxiv.org/pdf/1711.02782.pdf) and demostrate that it can lead into faster models with comparable accuracy.

### Dark knowledge (for 35 points out of 50)

Implement and test effect of using dark knowledge (http://www.ttic.edu/dl/dark14.pdf), in other words:

* Train a big network
* Use output probabilities of big network to help with training of smaller network
* Compare it to training small network without help of big network probabilities

There is a less risk here, so less points :)

### Bayesian neural nets

Take a very simple dataset (simpler than MNIST). Use PyMC3 to estimate distribution of neural network parameters.
Demostrate, than this distrubution gives you something useful (TODO ideas).
