# Background information

In this document we will point you to some useful background information to get you acquainted with the uses Hardware and Software

<!--
## Jetson Nano

![](https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano-2GB/getting_started/Jetson-nano-labeled-01.png)


https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit

The link above give some basic information as it gives some installation/ connection and usage information.

For this course we prepared a Specific image to be placed on your SD-card, which is an adapted version of the standard image of NVidia.

**So do NOT install the standard image on the SD card.**

We will run the Jetson in *Headless mode*, that means no screen / keyboard / mouse is required. Initial connection will be made over an USB cable to your laptop, additional communication will be over WIFI.

### Additional hardware

You will receive the following hardware for this project, You can use the hardware during the course at school or at home.
- Jetson Nano 2GB development board
- WIFI dongle (included with the Jetson)
- Casing for the Jetson (to be assembled) [Assembly instructions are Here](https://www.okdo.com/wp-content/uploads/2021/03/assembly-instructions-OKdo-Jetson-nano2-GB-Metal-case.pdf)
- SD card of 32 GB (the provided image only works on 32GB)
- Power supply (usb-c)
- Camera (you will get this a bit later)
- USB cable to connect the Jetson to your laptop



***All components should be returned after the course, after return the course grades will be finalized!***


## Docker:

On the Jetson we already pre-installed some [docker](https://www.docker.com/) containers, these are environments that contain all needed packages for running the assignments. The docker containers cannot be modified and always start at a default state, this means changes made to the docker environment will be lost on when leaving the docker environment.
The docker images will contain a shared folder where you can save your project data to, this then will be stored on your SD card.

You have to login to the Jetson and start the needed docker environment yourselves, as we have different environment for the different assignments.

-->

## Software packages:

We will use Python during this course as programming language, in addition we will uses several software packages and tools.
https://www.python.org/

### Jupyter notebook

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. https://jupyter.org/

### Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. https://matplotlib.org/

### Pandas
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. https://pandas.pydata.org/

### scikit-learn
Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities.
https://scikit-learn.org/
