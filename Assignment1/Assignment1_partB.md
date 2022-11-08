# Assignment 1 part B

## Human Activity Recognition

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.PS0Pv2vn_mk0Zhh7BxCJCgHaDy%26pid%3DApi&f=1)

In this assignment you will get to train, identify, compare, test and deploy machine learning algorithms (models) that will be able to recognize certain human activity movements.
This task is divided into two Assignments (Part B and Part C). In Part B you will use an UCI standard dataset for Human Activity Recognition (HAR). In Part C, you will get to create your own dataset. What we mean with your own dataset is that you get to choose the movements to perform, you record the data of each of those movements and then follow the same steps performed for the UCI HAR dataset for classifying your own movements.

The UCI standard dataset for Human Activity Recognition (HAR) has 6 basic human activities:
* Walking
* Sitting
* Standing
* Laying
* Walking Upstairs
* Walking Downstairs

The UCI HAR dataset is a good introduction to machine learning because of its intrinsic simplicity of human motions, such movements share several similarities when compared in terms of the values sensed.
It is challenging to differentiate from sitting and standing as well as from walking upstairs and walking downstairs. With such similar and simple movements, researchers needed to calculate several features for
finding how to differentiate them, for example, they even calculated the Entropy of each component of the Acceleration (after researching, there is no real explanation of why or how they did it, so, just use it!)



---

## UCI HAR dataset (part B)

![](https://img-blog.csdnimg.cn/20200228210007296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTY1Mzk0OA==,size_16,color_FFFFFF,t_70)

The UCI HAR dataset used is divided into train.csv and test.csv. You can get to know more about the UCI HAR dataset [Here](./Dataset/A%20Public%20Domain%20Dataset%20for%20Human%20Activity.pdf). You are required to perform all the steps described in the given Notebook
and remember that you always have to normalize your data (if needed) and perform dimensionality reduction (if possible). Not doing so, will influence your final mark, to avoid getting a reduction, it is recommended to calculate the correlation matrix and identify which features are highly correlated. Remember that most features are expressed as components of x, y and z.
You can use the following [Example](https://www.kaggle.com/dixittrivedi/humanactivityrecognition/notebook) for performing all the needed steps while getting to train, test, identify and deploy your ML models.

You can find the jupyter notebook here. The notebook contains the assignment description!

> [Assignment1_PART_B.ipynb](Assignment1_PART_B.ipynb)

Follow the required steps described, place comments/conclusions/insights per step and answer the given questions in the Notebook.
