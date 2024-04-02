In this homework, we will test the neural networks' ability to recognize some formal languages.
An example of formal language is, e.g., set of all palindromes (AA, ABA, ABBA, BAAB, ...).
Your network will classify whether the string belongs or does not belong to the language.

You should do the following:
* Pick a formal language (it should be at least a little bit interesting).
* Write a generator, which, for a given length, generates samples from the language and also samples outside of the language (some negative samples should also be close to the language, so they are hard to recognize).
* Pick either recurrent neural network architecture, a transformer, or some Mamba.
* Pick a fixed length of words L (should be long enough so that all words do not fit into memory easily).
* Train neural network and show that it can recognize your language for fixed length with decent accuracy (if it does not, either shorten the length, simplify language, or make the network bigger)
* Now try to analyze one of the following:
  - What is the relationship between L and the smallest network size, which can learn the task? Does it help to pre-train the network on smaller lengths first?
  - Can the network generalize to unseen lengths (either longer or shorter)? Does this improve if you train in on multiple input lengths?


You should submit:
* Code
* A simple report summarizing the results. These should be a description of your selected language, neural network architecture, tables/graphs with results and a quick discussion.
