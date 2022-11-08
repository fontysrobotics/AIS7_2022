# Assignment 1 part C

## Custom Activity Recognition

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.PS0Pv2vn_mk0Zhh7BxCJCgHaDy%26pid%3DApi&f=1)

In this assignment you will get to train, identify, compare, test and deploy machine learning algorithms (models) that will be able to recognize certain human activity movements.
This task is divided into two Assignments (Part B and Part C). In Part B you will use an UCI standard dataset for Human Activity Recognition (HAR). In Part C, you will get to create your own dataset. What we mean with your own dataset is that you get to choose the movements to perform, you record the data of each of those movements and then follow the same steps performed for the UCI HAR dataset for classifying your own movements.

---

## Your Own dataset

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.F4UEmSXsMa0mWrbMPjR30gHaD4%26pid%3DApi&f=1)

For this part of your assignment you will create your own dataset that consist of at least 3 distinct motions, for doing so you must use a phone app called [Phyphox](https://phyphox.org/) which allows you to create your own experiment and record the sensors in your phone. Please record your Accelerometer (x, y, z) and Giro (x, y, z) information using the App as shown in the image below.

![](https://lh3.googleusercontent.com/LBkwIPcoxHNI_2Q8RJgOam7hgQFvzA-vgvVsl8sVGR3jdT4g_iMhxJSNwABbl-PQIQ=w720-h310)

## Record your Phone motions with Phyphox
Please perform **motions that are not similar to the ones used in part B**, neither that are static or too similar to each other. You must record at least 3 distinctive classes/motions, like for example: the motion of making the number 1 and the motion of making the number 2, etc. Or jumping, riding a bike, rotating in place, etc. Please be creative!
Be aware that your dataset might be bias if only one of you perform all the motions.

![](https://www.ifolor.ch/content/dam/ifolor/inspire-gallery/tipps-tricks/malen-mit-licht/inspire_lightpainting13_zusatz2_620px_INT.jpg)

Phyphox will generate 2 files with sensor data, one for the Accelerometer and one for the Giro. Both files will have timestamps which might not match the recorded sensor data for each sensor. Please, preprocess and merge the files for using it as your dataset for training, testing and deploying your own supervised learning model.

You can find a jupyter notebook here. The notebook contains the assignment description!

> [Assignment1_PART_C.ipynb](Assignment1_PART_C.ipynb)

Follow the required steps described, place comments/conclusions/insights per step and answer the given questions in the Notebook.
