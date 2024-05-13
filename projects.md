# Final projects suggestions

Expected output:

* Runnable code (provide a list of dependencies).
* 2-3 pages long report, summarizing the results and methods.

A good project is, for example, a replication of some other results in a simplified setting (smaller dataset, networks, ...).
But it does not have to be; if you are not sure, ask.

## Deeper analysis of HW2

Analyze what are the individual (groups) of neuron computing. What is attention looking at (if you have a transformer)?
How is this formed during training? 

## Notautoregressive text generation

Most of the time we are generating text by producing one token after another (and new token probability depends on previous generated tokens). But maybe some other method is better (like <https://arxiv.org/pdf/2002.08926.pdf>).
You may try to generate some simple formal language.

## Optimizing nondifferential metrics

In many cases we care about one metric, which is non diffirentiable but optimize some other differentiable metrics. Typical case is machine translation where we evaluate BLEU score but optimize crossentropy (see <https://arxiv.org/pdf/1511.06732.pdf>).
Your goal is to pick a simple example task, where you can demonstrate that finetuning relevant metric can lead to better result, then only training on surrogate metric.

## Small LLM on CPU

I want to run an LLM only on CPU. Take something small (Llama-7B, Phi-2) and try to figure out the fastest way how to run it on the CPU.
Look outside of just reference Pytorch implementation (e.g. check llama.cpp). Does increasing batch size help?
Does quantization help? Where are the bottlenecks (try running a profiler and check whether you are stuck on memory-cache loading or on computation).

## Small LLM on small GPU

Same as above, but you also have a GPU where the model does not fit as a whole. 

## Finetuning with a small amount of data

It is possible that if you have a small amount of labeled data, the finetuning of the whole model might overfit.
Take VTAB-1k benchmark, some method cited in Table 2 here https://arxiv.org/pdf/2403.19067 and reproduce results (maybe on smaller ViT or Resnet).

## Is Llama-3 sensitive to quantization

There is a rumor, that Llama-3 does not like quantization.
Take nonquantized Llama2-7B and Llama3-8B and their versions quantized to 4 bits.
Figure out whether Llama3 is more sensitive to quantization or not.

## Your own idea

Send me an email and we will see.
