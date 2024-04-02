In this homework, we will test the neural networks' ability to recognize some formal languages.
An example of formal language is, e.g., set of all palindromes (AA, ABA, ABBA, BAAB, ...).
Your network will do a binary classification of whether the string belongs or does not belong to the language.

You should do the following:
* Pick a formal language (it should be at least a little bit interesting).
* Write a generator, which for given length generates samples from the language and also samples outside of the language
* Pick either recurrent neural network architecture, a transformer, or some Mamba.
* Pick a fixed length of words (should be long enough, that all words do not fit into memory easily).
* Train neural it and show that it can recognize your language for fixed length with decent accuracy (if it does not, either shorten the length, simplify language, or make the network bigger)
* 


You should submit:
* Code
* A simple report summarizing the results. These should be a description of your selected language, neural network architecture, tables/graphs with results and a quick discussion.
