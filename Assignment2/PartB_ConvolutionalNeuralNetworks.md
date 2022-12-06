# Convolutional Neural Network (CNN)

In this part of the assignment you will create and test a small [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN).
Such a network can train directly from image data, so the feature extraction is done in the convolutional part, where the classification is done in a fully connected Neural Network.

![](https://miro.medium.com/max/2000/1*vkQ0hXDaQv57sALXAJquxA.jpeg)

Before you start it is wise to follow the tutorials below, after that you can go to the assignment.

---

## Tutorial
In the given tutorials you will learn how to build and train a CNN that can distinguish images of Cats and Dogs.

In the video below you will see the first steps of preparing the given dataset

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/j-3vuBynnOE/0.jpg)](https://www.youtube.com/watch?v=j-3vuBynnOE)

https://youtu.be/j-3vuBynnOE

The next video you will learn how to create and train a CNN (See notes below)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/WvoLTXIjBYU/0.jpg)](https://www.youtube.com/watch?v=WvoLTXIjBYU)

https://youtu.be/WvoLTXIjBYU

In addition of this tutorial we want you to visualize the some of the outputs so they are more meaningful/understandable. This is shown in the [Tips & Tricks](TipsAndTricks.md) section


**NOTE:**

<!--
Due to processing/memory limitations please
* Use the providend dataset with limited training images (2.5k per class)
( you can delete the not needed images of the downloaded dataset, or fetch the reduced dataset from the MSTeams environment)
* Reduce the convolutions to max 16 instead of 256 in the example
* Reduce the dence layer to 16 instead of 64 in the example
-->

* The last Dense layer in the example is missing a Relu activation, you should add this

---

## Assignment

In this assignment you will create your own Convolutional Neural Networks (CNN) model and train custom images on it.

| Before you start the assignment make sure you followed the above tutorials. |
| ---|

You can find the jupyter notebook here. The notebook contains the assignment description!
> [Assignment2_PART_B.ipynb](Assignment2_PART_B.ipynb)

Follow the required steps described, place comments/conclusions/insights per step and answer the given questions in the Notebook.

---

## Hints


Additional info can be found in the [tips and tricks](TipsAndTricks.md) document
