# Homework variant A

## General description

Design a neural network, which discriminates between sequences with regular and irregular gaps.
We will work over simple binary sequences, where 0 means nothing and 1 means a signal pulse.

Regular sequence is one where gaps between pulses are constant, something like this: "000100001000010000100"
Irregular sequence is one where gaps between pulses are not constant, something like this: "0001001000000101000000100"

The task is obviously complicated by the fact, that sometimes the gap between pulses is not strictly integral, so a regular sequence might also look like: "0001000100100010010001"

The frequency of the signal can vary slightly over time.

And there also might be noise, so sometimes 1 is flipped to zero and vice versa.

## Easy difficulty (50% points)

All sequences are of length 1000 (if you want to hardcode this, you can).
All sequences are either regular or completelly irregular (generated with default parameters from generator.py).
To evaluate just run `python evaluate.py --data eval_easy.json`

## Hard diffuculty

Evaluation sequences have different length.
Some sequences are only partially irregular (irregularities can occur intermittently), these count as irregular.
Regular and irregular parts are generated with default parameters from generator.py.

To evaluate just run `python evaluate.py --data eval_hard.json` (don't forget to unzip first).

TODO: target metrics

## Evaluation, training setup and what should you submit

There two files eval_easy.json and eval_hard.json with evaluation sequences.
There is also evaluate.py, which will be used to evaluate your model (do not edit this).
There is also placeholder file model.py, which you should fill out with your model (in the create_model function).
And there is also train.py, which you can use to train your model (you can edit this as you like).

You should submit model.py, train.py files plus your model checkpoint (model.pth), which will be loaded with evaluate.py. Plus submit a short text file describing techniques you used.

## Allowed and disallow techniques

Do not use FFT. Do not train on test.
Any type of convolutional, recurrent networks or transformers is allowed.
You can use AI as you wish, but describe how you use it and keep in mind, that you must understand everything inside your solution.
Also, if you want to use autoresearch by Andrej Karpathy, knock yourself out.
