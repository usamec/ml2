## Schedule

* Tuesday 9:50-11:20 I-23
* Wednesday 13:10-14:40 M-V

## Contact

`<surname>@fmph.uniba.sk`

## Grading

Three projects:
* [Autograd](https://usamec.github.com/ml2/hw1) - 20% - deadline 9th March 
* [QRNN](https://usamec.github.com/ml2/hw1) - 30% - deadline end of semester (20th May)
* Replication of recent paper results - 50%

Getting less than 50% from autograd project -> FX.
Otherwise typical grading scheme (more than 90% - A, 89% - 80% - B, ..., 59 % - 50% - E, less than 50% - FX).

## Recommended prerequisites

* Either Machine learning or Neural networks course (ideally both)
* No fear of math (gradients)
* Reasonable coding skills in Python

## Good other courses

* http://ttic.uchicago.edu/~shubhendu/Pages/CMSC35246.html
* https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/
* http://www.cs.toronto.edu/~rgrosse/courses/csc321_2017/

## Schedule

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
