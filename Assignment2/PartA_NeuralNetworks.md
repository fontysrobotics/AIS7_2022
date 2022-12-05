# Assignment 2 - Part A
---
## Fully Connected Neural Network: MNIST dataset
---

In this part of the assignment you will implement your own fully connected neural network using [Keras](https://keras.io/).

Keras is an API designed for human beings, not machines. So it is a more accessible method of easily creating and using Neural Network architectures. Under the hood Keras uses [Tensorflow](https://www.tensorflow.org/), which is more complex in use.

---

## Tutorial

You are first going to build a Neural Network that is capable of classifying handwritten numbers. For this the [MNIST database](https://en.wikipedia.org/wiki/MNIST_database) is used, here an example of some of the training data.

![](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)


In the following video tutorial the basics of how to create/train/test a fully connected Neural Network and apply it to this database are explained to you.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/wQ8BIBpya2k/0.jpg)](https://www.youtube.com/watch?v=wQ8BIBpya2k)

https://youtu.be/wQ8BIBpya2k


In addition of this tutorial we want you to visualize the some of the outputs so they are more meaningfull/understandable. This is shown in the Tips & Tricks section

---

## Assignment

| Before you start the assignment make sure you followed the above tutorials. |
| ---|

In this Assignment you are going to classify images from a fashion dataset.

<!--
[Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. We intend Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.
-->
<!--
![](https://machinelearningmastery.com/wp-content/uploads/2019/02/Plot-of-a-Subset-of-Images-from-the-Fashion-MNIST-Dataset-1024x768.png)
-->




<!--
### Tasks

* Create a Jupyter notebook in where you build and train a fully connected Neural Network that can classify the fashion_mnist dataset.
  * Describe the implemented network architecture.
  * How many parameters does this network have, and where in the network are these located?
  * Visualize & explain the learning curves (loss, accuracy)
  * Explain what hyperparameters are available and what they do.
  * Which hyperparameter result in better training results?
  * What is the final accuracy of the trained Network?
  * In which way could the network accuracy be improved further (only explanation, no implementation)?
* The notebook should contain al code, outputs and answers to the given questions (so make sure we can find all needed info)
-->


You can find the jupyter notebook here. The notebook contains the assignment description!

> [Assignment2_PART_A.ipynb](Assignment2_PART_A.ipynb)

Follow the required steps described, place comments/conclusions/insights per step and answer the given questions in the Notebook.

---
## Hints

You can import the dataset directly from keras
```
fashion_mnist = keras.datasets.fashion_mnist

```  

References:
* [Neural Networks: parameters, hyperparameters and optimization strategies](https://towardsdatascience.com/neural-networks-parameters-hyperparameters-and-optimization-strategies-3f0842fac0a5)

Additional info can be found in the [tips and tricks](TipsAndTricks.md) document
