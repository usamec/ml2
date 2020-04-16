## Covid closure

We have a facebook group for comunication:
<https://www.facebook.com/groups/544273583166584/>

Things you should get familiar with:

### Machine translation
* See <http://web.stanford.edu/class/cs224n/> mainly: Lecture8 about machine translation. Get familiar with sequence to sequence models, beam search decoding and attention.

### Speech recognition (mainly CTC and Transducers)
* Get familiar with Connectionist temporal classification and Transducers. <https://www.youtube.com/watch?v=3MjIkWxXigM>
* I also recommend checking <https://arxiv.org/pdf/1211.3711.pdf> and <http://www.cs.toronto.edu/~hinton/absps/DRNN_speech.pdf>.

### Self-attention and transformers
* Again <http://web.stanford.edu/class/cs224n/> lecture 10

### Bayessian modeling
* Check out PyMC3 tutorial <https://docs.pymc.io/notebooks/getting_started.html> (there will be more content about this comming soon).

## Schedule

* Tuesday 11:30-13:00 F1-247
* Thursday 9:50-11:20 M-X

## Contact

`<surname>@fmph.uniba.sk`

## Grading

Three projects:
* [Autograd](https://usamec.github.com/ml2/hw1) - 20% - deadline 9th March 
* Relativelly simple implementation of something exotic. [Lottery tickets](https://usamec.github.com/ml2/hw2) - 30% - deadline end of semester (15th May)
* [Final project](https://usamec.github.io/ml2/projects) aka Replication of recent paper results - 50%
  * General deadline 18th June
  * Deadline for 5th year students - 20th May

Getting less than 50% from autograd project -> FX.
Otherwise typical grading scheme (more than 90% - A, 89% - 80% - B, ..., 59 % - 50% - E, less than 50% - FX).

## Recommended prerequisites

* Either Machine learning or Neural networks course (ideally both)
* No fear of math (gradients)
* Reasonable coding skills in Python

## Good other courses

* <http://ttic.uchicago.edu/~shubhendu/Pages/CMSC35246.html>
* <https://fleuret.org/ee559/> and <https://fleuret.org/ee559-2018/dlc/>
* <http://www.cs.toronto.edu/~rgrosse/courses/csc321_2017/>
* <http://introtodeeplearning.com/>

## Schedule

Similar to old. We will skip things over graphs (except semisupervised learning).
We will probably add more about model compression and deployment (quantization).

Calculus for deep learning: <https://explained.ai/matrix-calculus/>

### 18. 2

* Introduction to DL. https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1a-introduction.pdf, http://ttic.uchicago.edu/~shubhendu/Pages/Files/Lecture1_pauses.pdf
* Typical modelling problem, which consist of:
  * parametrized function, which takes input and output prediction
  * loss function, which takes prediction and required output and outputs loss
  * optimizer, which find parameters with smallest loss as possible
* Pytorch demos

### 20. 2

* Optimization algorithms and initialization. Slides from: http://ttic.uchicago.edu/~shubhendu/Pages/Files/Lecture6_flat.pdf, https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-5-init-optim.pdf
* About network initialization: http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf

### 25. 2

* Building blocks of neural networks
* Fully-connected (Pytorch Linear, Keras Dense) layers
* Convolutional layers
* Maxpooling

### 27. 2

* Recurrent neural networks, GRU, LSTMs
* Difficulty of training them 

### 3. 3

* Relu
* BatchNormalization, LayerNormalization
* [ResNets](https://arxiv.org/pdf/1512.03385.pdf)

### 5. 3

* [Object detection](http://imatge-upc.github.io/telecombcn-2016-dlcv/slides/D3L4-objects.pdf), [more material](https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/object_localization_and_detection.html)

## Old schedule

### 20.2.
* Introduction to DL. https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1a-introduction.pdf, http://ttic.uchicago.edu/~shubhendu/Pages/Files/Lecture1_pauses.pdf
* Typical modelling problem, which consist of:
  * parametrized function, which takes input and output prediction
  * loss function, which takes prediction and required output and outputs loss
  * optimizer, which find parameters with smallest loss as possible

### 21.2.

* Demonstration of theano and chainer (TODO notebooks)
* How backprop works

### 27.2

* Optimization algorithms and initialization. Slides from: http://ttic.uchicago.edu/~shubhendu/Pages/Files/Lecture6_flat.pdf, https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-5-init-optim.pdf
* About network initialization: http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf
* Neural nets can fit anything: https://arxiv.org/pdf/1611.03530.pdf
* Small batch generalizes better than large batch: https://openreview.net/pdf?id=HkmaTz-0W

### 28.2

* Details from [Understanding the difficulty of training deep feedforward neural networks
](http://proceedings.mlr.press/v9/glorot10a.html)
* Tricks for deep architectures:
  * Good initialization (see paper above)
  * Batch norm (see last lesson)
  * Relu units
  * Residual networks (just google it)
* Talking about vanishing and exploding gradients [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf)
* [LSTM](http://web.eecs.utk.edu/~itamar/courses/ECE-692/Bobby_paper1.pdf), [GRU](https://arxiv.org/pdf/1412.3555.pdf), [IRNN](https://arxiv.org/pdf/1504.00941.pdf)
* [Highway networks](https://arxiv.org/pdf/1505.00387.pdf)

### 6.3

* Generaliation in neural networks and dropout: [slides](http://www.cs.toronto.edu/~rgrosse/courses/csc321_2017/slides/lec9.pdf), [slides 19-25](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-6-going-deeper.pdf). 


### 7.3

* Language generation: [char-RNN](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* Machine translation. Best course for that is [CS224n](http://web.stanford.edu/class/cs224n/syllabus.html). Relevant slides are [1](http://web.stanford.edu/class/cs224n/lectures/lecture10.pdf), [2](http://web.stanford.edu/class/cs224n/lectures/lecture11.pdf), [3](http://web.stanford.edu/class/cs224n/lectures/lecture12.pdf)

### 13.3

* [ResNets](https://arxiv.org/pdf/1512.03385.pdf)
* Making convolutions smaller [Inception](https://arxiv.org/pdf/1512.00567.pdf), [more inception](https://arxiv.org/pdf/1602.07261.pdf)
* [Object detection](http://imatge-upc.github.io/telecombcn-2016-dlcv/slides/D3L4-objects.pdf), [more material](https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/object_localization_and_detection.html)

### 14.3
* [making nnets faster](https://usamec.github.com/ml2/RG%20slides.pdf)

### 20.3

* [Generative adversarial networks](http://slazebni.cs.illinois.edu/spring17/lec11_gan.pdf)
* [Wasserstein GAN](https://www.alexirpan.com/2017/02/22/wasserstein-gan.html), [Wasserstein GAN 2](https://lilianweng.github.io/lil-log/2017/08/20/from-GAN-to-WGAN.html)

### 21.3

* Introduction to Bayesian modelling
* Mostly stuff from [here](https://github.com/oapio/PrecisionWorkshop1_Prep/tree/master/notebooks)

### 27.3

* Sampling methods for probabilistic models
* Rejection sampling
* Importance sampling
* MCMC sampling

### 28.3

* MCMC sampling in more detail
* Metropolis and Metropolis hastings
* Gibbs sampling

### 4.4

* PyMC demos

### 10.4

* Reinforcement learning
* [slides 1](https://icml.cc/2016/tutorials/deep_rl_tutorial.pdf), [slides 2](https://people.eecs.berkeley.edu/~pabbeel/nips-tutorial-policy-optimization-Schulman-Abbeel.pdf)

### 11.4

* Reinforcement learning demos

### 17.4

* Graphs in ML
* [Smart reply for google inbox](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45189.pdf)

### 18.4 and 24.4

* [Graphs in ML course](http://researchers.lille.inria.fr/~valko/hp/mva-ml-graphs.php)
* Selected topics from lecture 1-4

### 2.5

* no lesson

### 9.5

* Neareast neighbours
* [nmslib](https://github.com/nmslib/nmslib)

### 15.5, 16.5

* lecture canceled. If you have any questions about project send me an email and we can meet.
