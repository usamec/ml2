Using your framework of choice, implement [Lottery ticket hyphothesis](https://arxiv.org/pdf/1803.03635.pdf).
Its up to you which architecture (couple fully-connected layers, convolution network) you choose. Also choice of dataset is up to you (MNIST/CIFAR10 is recommended).

Expected output: Program which:

* downloads the dataset (when needed)
* runs training on dataset
* finds sparsity pattern
* runs training of sparse part with original initialization
* runs training of sparse with random initialization
* compares results

Also the implementation should be mainly yours (especially the sparsity part). 

Tips and tricks:

* For sparsity you can either use custom layers, which hid parameters behind mask, or...
* Just set weights to zero after each iteration

Bonus points:
* Tuning sparsification (couple of iterations for sparsification).
