#!/usr/bin/env python

#Import Libraries
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import time
import sys

#Setup Modbus Connection
client = ModbusClient('localhost', port=5020)
UNIT=0x1        #Address of the slave to control

client.connect()

#Main Loop
while True:
    speed = input("Enter a speed from -1 to 1: \n")     #Takes user input
    speed = int((speed*10)+10)                          #Modbus only accepts positive ints, so we convert to and int between 0-20
    client.write_register(1, speed, unit=UNIT)


