Using your framework of choice, implement [Quasi-recurrent neural network](https://arxiv.org/pdf/1611.01576.pdf).
You can choose which type of QRNN you will implement (f, fo, ifo). As for the dataset pick one of the following:

* character language modelling (similar to char-rnn we talked above), you can choose any corpus you like
* sentiment prediction (like [imdb movie reviews](http://ai.stanford.edu/~amaas/data/sentiment/))

Expected output: Program which:

* downloads the dataset (when needed)
* runs training on datasets
* generated some samples (in character language modelling), generates predictions on test datasets and calculates accuracy

Also the implementation should be mainly yours (especially the QRNN part).

Tips and tricks:

* some frameworks do not have 1D convolution and you need to use 2D convolution of 1xw shape and couple of reshapes around
* you need to use some padding to keep input and output of the convolution same. The padding is usually named either 'same' or 'half'.
* in case of sentiment prediction, your input would be sequence of one hot vectors. Try to use sparse capabilities of your framework. Or use word embeddings first.
