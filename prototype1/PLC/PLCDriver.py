#!/usr/bin/env python3

import configparser
import importlib
import time
import PLCLogic

#Declare a dict to hold level 0 device drivers
device_list = {}
#Declare a dict to hold a parameter names and register addresses
param_list = {}

def init():

    #Read the config file into config object
    config = configparser.RawConfigParser()
    file = r'config.txt'
    config.read(file)

    #Sets the address of this device from config
    address = config.get('address','address')

    #Loads device drivers specified in config
    for device in config.items('device drivers'):

        class_name = device[1]                                                          #Loads driver classname for device
        device_class = getattr(importlib.import_module(class_name), class_name)         #Imports the class and stores the class object in device_class
        device_driver = device_class()                                                  #Intialises an object of the driver class and stores in device_driver
        device_list.update({device[0]:device_driver})                                   #Stores the device name and driver object in device_list

    param_list.update(config.items('parameter addresses'))

def writeModbus(register,value):
    time.sleep(0.00001)
def readModbus(register):
    time.sleep(0.00001)

def main():

    init()
    PLCLogic.main(device_list, param_list, writeModbus, readModbus)


if __name__ == "__main__":
    main()
