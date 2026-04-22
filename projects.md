# Final projects

## General rules

Expected output:

* Runnable code (provide a list of dependencies).
* 5-7 pages long report, summarizing the results and methods.

Can be done by a single person or in a team of two (then a longer report and more work is expected).

The general workflow is: You submit a project, we will talk to you about it, and tell you the points forthe  current state, plus give you pointers for possible improvement. After the deadline for improvement, you will get your points.

## Deadlines for 5th year students

* Project deadline: 17th May
* Oral exam + feedback: around 20th May
* Final corrections: 26th May

## Deadlines for others

* Project deadline: 1st June
* Oral exam + feedback: around 4th June
* Final corrections: 15th June

## Suggested project topics

A good project is, for example, a replication of some other results in a simplified setting (smaller dataset, networks, ...) or
analysis or some behaviour of a neural network. But it does not have to be; if you are not sure, ask.



* RNN with state dependended forget gate vs just input dependent. (Aka SSM vs GRU). (https://x.com/francoisfleuret/status/2031633024253624698)

### Efficient KL-divergence implementation

Expand efficient cross-entropy loss implementation <https://arxiv.org/abs/2411.09009> to KL-divergence.
I.e., given two sets of embeddings E1 and E2, and output weight matrices W1, W2 (where W1 is fixed), we want to optimize KL(E1W1, E2W2) without materializing the whole E1W1 or E2W2.
The goal here is not speed (I am fine with 2x slower than PyTorch KLDiv), but low memory consumption.
But it should be more effort than just a couple of Pytorch hacks (i.e., you should do Triton or CUDA).

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
