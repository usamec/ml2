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

## Your own idea

Send me an email and we will see.
