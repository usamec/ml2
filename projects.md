# Final projects suggestions

Expected output:

* Runnable code (provide list of dependencies).
* 1-2 pages long report, sumarizing the results and methods.

## 3D reconstruction via neural nets

Something like <http://openaccess.thecvf.com/content_cvpr_2017/papers/Sinha_SurfNet_Generating_3D_CVPR_2017_paper.pdf>.

## Rendering improvement via neural nets

Goal: render scene via ray tracing with low sample count and improve via neural net.
See: <https://arxiv.org/pdf/1803.04189.pdf> <https://dl.acm.org/doi/10.1145/2766977>

## Adversarial examples generation for text

Do adversarial attack for some text classifier like <https://openreview.net/pdf?id=r1QZ3zbAZ>.

## Notautoregressive text generation

Most of the time we are generating text by producing one token after another (and new token probability depends on previous generated tokens). But maybe some other method is better (like <https://arxiv.org/pdf/2002.08926.pdf>).
Goal here is to implement and test some either language translation, generation or speech recognition, which does not generates text one by one.

## GAN and natural langauge

Implement some GAN which generates text (choice is up to you).

## Optimizing nondifferential metrics

In many cases we care about one metric, which is non diffirentiable but optimize some other differentiable metrics. Typical case is machine translation where we evaluate BLEU score but optimize crossentropy (see <https://arxiv.org/pdf/1511.06732.pdf>).
Your goal is to pick a simple example task, where you can demonstrate that finetuning relevant metric can lead to better result, then only training on surrogate metric.

## Conditional computation

Take a paper about conditional computation (https://arxiv.org/pdf/1701.06538.pdf, https://arxiv.org/pdf/1511.06297.pdf, https://arxiv.org/pdf/1308.3432.pdf, https://arxiv.org/pdf/1611.01144.pdf) and do following things:

* Take a simple dataset (like MNIST or CIFAR-10, ...)
* Train some simple nonconditional model M1
* Train conditional model M2 with similar computational cost (prediction time) as M1

The goal is to have much better accuracy of M2 model than M1. Also they should be quite similar in other architecture considerations (like both should be convnets, or fully connected nets, ...).
It might help to have custom implemention of prediction outside of the tradional frameworks.

## Sparsification

Apply sparsification techniques from some paper (https://arxiv.org/pdf/1711.02782.pdf) and demostrate that it can lead into faster models with comparable accuracy.
It might help to have custom implemention of prediction outside of the tradional frameworks.

## Dark knowledge (for 35 points out of 50)

Implement and test effect of using dark knowledge (http://www.ttic.edu/dl/dark14.pdf), in other words:

* Train a big network
* Use output probabilities of big network to help with training of smaller network
* Compare it to training small network without help of big network probabilities

There is a less risk here, so less points :)

## Bayesian neural nets

Take a very simple dataset (simpler than MNIST). Use PyMC3 to estimate distribution of neural network parameters (see here http://twiecki.github.io/blog/2016/06/01/bayesian-deep-learning/).
Demostrate, than this distrubution gives you something useful, for example:

* less overfitting
* uncertanity in predictions
* etc.

## Learning with unlabeled data

Take a dataset for sentiment, take only small amount of labeled samples (like 100 or 1000) and delete labels from other samples. Compare:

* [semisupervised sequence learning](https://arxiv.org/abs/1511.01432)
* semisupervised learning using graphs [like here](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45189.pdf)
* training only using labeled data (that small sample)(using method of your choice)

## Your own idea

Send me an email and we will see.
