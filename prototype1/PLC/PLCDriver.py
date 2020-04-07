#!/usr/bin/env python3

import configparser
import importlib
import time
import PLCLogic

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def load_config():

    #Read the config file into config object
    config = configparser.RawConfigParser()
    file = r'config.txt'
    config.read(file)

    return(config)

def load_devices():

    device_list = {}

    #Loads device drivers specified in config
    for device in config.items('device drivers'):

        class_name = device[1]                                                          #Loads driver classname for device
        device_class = getattr(importlib.import_module(class_name), class_name)         #Imports the class and stores the class object in device_class
        device_driver = device_class()                                                  #Intialises an object of the driver class and stores in device_driver
        device_list.update({device[0]:device_driver})                                   #Stores the device name and driver object in device_list

    return(device_list)

def load_client():

    server_ip = config.get('server','ip')
    server_port = config.get('server','port')

    client = ModbusClient(server_ip,server_port)
    client.connect()

    return(client)

#Loads the config file
config = load_config()
#Loads a dict that contains device names and addresses
device_list = load_devices()
#Loads a dict that holds parameter names and register addresses
param_list = {}
param_list.update(config.items('parameter addresses'))
#Loads a string to hold the address of this device
address = int(config.get('address','address'),16)                                   #Parses from hex (base 16)
#Loads and initialises the modbus connection
client = load_client()

def writeModbus(register,value):
    client.write_register(register,value,unit=address)
def readModbus(register):
    registers = client.read_holding_registers(register,unit=address)
    return(registers.registers[0])

def main():

    PLCLogic.main(device_list, param_list, writeModbus, readModbus)


if __name__ == "__main__":
    main()