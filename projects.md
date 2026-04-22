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
an analysis of some behavior of a neural network. But it does not have to be; if you are not sure, ask.

A bad project is something like: "I trained a basic CNN on CIFAR-10, here are the results." Basically, if a good LLM can one-shot it, it is not good.

### LLM compression for a specific task

Pick a small LLM (e.g. SmolLM2 is a good choice) and a highly specific task (e.g., extracting movie times from a movie theater page).
Try compressing the language model as much as possible without changing the output of the task.
The compression method is up to you. Something specific (e.g., removing useless attention heads for the task) is more preferable than just generic 4-bit quantization.

### LLM destruction/interpretability for a specific task

Same as above, but we are asking what part of the network is absolutely necessary for the task (and is not super important in the general context).

### Switching optimizers during training (or between pretraining fine-tuning)

You would have to pretrain your own small LLM here (I recommend nanogpt speedrun from https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2024-10-18_PyTorch25/d4bfb25f-688d-4da5-8743-33926fad4842.txt).

Now we want to know whether switching from Muon to Adam and vice versa works.
Ideally, you want to pretrain an LLM to a specified loss (with both optimizers). Then you need to fine-tune that LLM on a specific task.
And try all combinations of optimizers (pretrain on Adam-finetune with Adam; pretrain with Adam-finetune with Muon; pretrain on Muon-finetune with Adam; pretrain with Muon-finetune with Muon). 
Do not forget to optimize the hyperparameters during finetuning.

### Efficient KL-divergence implementation

Expand efficient cross-entropy loss implementation <https://arxiv.org/abs/2411.09009> to KL-divergence.
I.e., given two sets of embeddings E1 and E2, and output weight matrices W1, W2 (where W1 is fixed), we want to optimize KL(E1W1, E2W2) without materializing the whole E1W1 or E2W2.
The goal here is not speed (I am fine with 2x slower than PyTorch KLDiv), but low memory consumption.
But it should be more effort than just a couple of Pytorch hacks (i.e., you should do Triton or CUDA).

## Capabilities of transformers/RNNs

Note for data science students: Check what a formal language is (i.e., regular and context-free language) <https://foja.dcs.fmph.uniba.sk/materialy/skripta.pdf>
Create a toy task that can be easily expanded for longer sequences. Good examples:

* Generating/recognizing correctly bracketed sequences (e.g. `([{}]((([]))))`)
* Key-value lookup with multiple queries (e.g.`k1v1k2v2k3v3k4v4#k2k3#v2v3` model should find `v2v3`)
* Check whether number of `a` and `b` is same in the input (e.g. `aaacbcbcb` is good)

Now you check the following:
* Is it even solvable for the transformer?
* Does it generalize to longer inputs? (with maybe an alibi positional embedding)
* What is the minimal size of a transformer to solve the task?
* What are attention heads looking at?

Another variant is with the Recurrent neural networks, here the question is:
"Is there a task where networks with state-dependent forget gate (GRU/LSTM) are better than networks without it (like SSM or Quasi-recurrent RNN)."

## Your own idea

Send me an email, and we will see.
