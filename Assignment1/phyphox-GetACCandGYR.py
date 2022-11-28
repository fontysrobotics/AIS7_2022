# interfacing with the phyphox app and its data

# === Seting up list of access names for each sensor and axis === #
M_CONTROLS_Acc = ["acc_X", "acc_Y", "acc_Z"] 	# Accelerometer axis names
M_CONTROLS_Gyr = ["gyr_X", "gyr_Y", "gyr_Z"] 	# Gyro axis names

# === Selecting the IP of the phone and seting up list of channels for each sensor and axis === #
PP_ADDRESS = "http://192.168.2.158:8080"	# Phone IP address
PP_CHANNELS_Acc = ["accX", "accY", "accZ"]	# Accelerometer axis channels
PP_CHANNELS_Gyr = ["gyrX", "gyrY", "gyrZ"]	# Gyro axis channels


import requests
import time

import pandas as pd


# --- Function for getting the data from the PhyPhox app
def getDataPhyphox ():

    # List to store the ais data in one place
    data_list = []
    
    # Create the request for the data for each sensor type
    url_ACC = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS_Acc))
    url_GYR = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS_Gyr))
    
    # Request data for each sensor
    data_ACC = requests.get(url=url_ACC).json()
    data_GYR = requests.get(url=url_GYR).json()
    
    # DBG
    # print ("\n\n=== New run ===")
    
    # -- Loop for Accelerometer to get all 3 channels (axis)
    for i, control in enumerate(M_CONTROLS_Acc):

        # DBG: Print channel number and name
        # print ("i = ", i, "; ", "control: ", control)
        
        # DBG: Print the data in the channel
        # print ("data: ", data_ACC["buffer"][PP_CHANNELS_Acc[i]]["buffer"][0])
        
        # Append data to the list
        data_list.append(data_ACC["buffer"][PP_CHANNELS_Acc[i]]["buffer"][0])
        
        

    # -- Loop for Gyroscope to get all 3 channels (axis)
    for i, control in enumerate(M_CONTROLS_Gyr):

        # DBG: Print channel number and name
        # print ("i = ", i, "; ", "control: ", control)

        # DBG: Print data in the channel
        # print ("data: ", data_GYR["buffer"][PP_CHANNELS_Gyr[i]]["buffer"][0])

        # Append data to the list
        data_list.append(data_GYR["buffer"][PP_CHANNELS_Gyr[i]]["buffer"][0])
        
        
    # DBG: Print the data list
    # print (data_list)
    
    # -- Create a datafram of the data with the names of the columns
    dataDF = pd.DataFrame([data_list], columns = M_CONTROLS_Acc + M_CONTROLS_Gyr)
    	
    # DBG: Print out the dataframe
    # print ("\n=== Data Frame ===\n", dataDF)
    
    # Return the dataframe to where it is needed
    return dataDF




while True:

    liveData = getDataPhyphox()
    print ("Live Data", liveData)
