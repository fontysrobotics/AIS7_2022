# Tips & Tricks (Neural Networks)

Here we provide you with some option to visualize you outputs

## plotting learningcurves

You can plot the training process, for this you have to save the training results after fitting in a history list.

```
history = model.fit(......)
```
This history you can plot

```
import pandas as pd
import matplotlib.pyplot as plt

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()

```
Will generate a plot like this
![](https://i.stack.imgur.com/LfFC3.png})

## Model Summary

You can show in a table the summary of your constructed network.

```
model.summary()

Layer (type)         Output Shape   Param #     Connected to                     
=====================================================================
flatten_1 (Flatten)   (None, 784)     0           flatten_input_1[0][0]            
dense_1 (Dense)     (None, 10)       7850        flatten_1[0][0]                  
activation_1        (None, 10)          0           dense_1[0][0]                    
======================================================================
Total params: 7850

```


<!--
## Monitoring the jetson processes

You can monitor the CPU and GPU, memory and Swap usage of your jetson with a pre-installed program called [Jtop](https://github.com/rbonghi/jetson_stats).
Start a new putty session and login to your jetson (do not start the docker from this session)

to start it type: $ jtop
![](Jtop.PNG)
-->
