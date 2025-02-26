# Final projects suggestions

Expected output:

* Runnable code (provide a list of dependencies).
* 2-3 pages long report, summarizing the results and methods.

A good project is, for example, a replication of some other results in a simplified setting (smaller dataset, networks, ...) or
analysis or some behaviour of a neural network. But it does not have to be; if you are not sure, ask.

## Efficient KL-divergence implementation

Expand efficient cross-entropy loss implementation <https://arxiv.org/abs/2411.09009> to KL-divergence.
I.e. given two sets of embeddings E1 and E2, and output weight matrices W1, W2 (where W1 is fixed) we want to optimize KL(E1W1, E2W2) without materializing the whole E1W1 or E2W2.

## Capabilities of transformers

Note for data science students: Check what is a formal language (i.e. regular and context-free language) <https://foja.dcs.fmph.uniba.sk/materialy/skripta.pdf>
Create some toy task, which can be easily expanded for longer sequences. Good examples:

* Generating/recognizing correctly bracketed sequences (e.g. `([{}]((([]))))`)
* Key-value lookup with multiple queries (e.g.`k1v1k2v2k3v3k4v4#k2k3#v2v3` model should find `v2v3`)
* Check whether number of `a` and `b` is same in the input (e.g. `aaacbcbcb` is good)

Now you check following:
* Is it even solvable for transformer?
* Does it generalize to longer inputs? (with maybe alibi positional embedding)
* What is minimal size of transformer to solve task?
* What are attention heads looking at?

## Finetuning with a small amount of data

It is possible that if you have a small amount of labeled data, the finetuning of the whole model might overfit.
Take VTAB-1k benchmark, some method cited in Table 2 here https://arxiv.org/pdf/2403.19067 and reproduce results (maybe on smaller ViT or Resnet).

## Your own idea

Send me an email and we will see.
