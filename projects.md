# Final projects suggestions

Expected output:

* Runnable code (provide a list of dependencies).
* 2-3 pages long report, summarizing the results and methods.

A good project is, for example, a replication of some other results in a simplified setting (smaller dataset, networks, ...) or
analysis or some behaviour of a neural network. But it does not have to be; if you are not sure, ask.

## Efficient KL-divergence implementation

Expand efficient cross-entropy loss implementation <https://arxiv.org/abs/2411.09009> to KL-divergence.
I.e. given two sets of embeddings E1 and E2, and output weight matrices W1, W2 (where W1 is fixed) we want to optimize KL(E1W1, E2W2) without materializing the whole E1W1 or E2W2.

## Deeper analysis of HW2

Analyze what are the individual (groups) of neuron computing. What is attention looking at (if you have a transformer)?
How is this formed during training? 

## Finetuning with a small amount of data

It is possible that if you have a small amount of labeled data, the finetuning of the whole model might overfit.
Take VTAB-1k benchmark, some method cited in Table 2 here https://arxiv.org/pdf/2403.19067 and reproduce results (maybe on smaller ViT or Resnet).

## Your own idea

Send me an email and we will see.
