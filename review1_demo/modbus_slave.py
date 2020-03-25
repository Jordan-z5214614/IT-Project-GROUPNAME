#!/usr/bin/env python3

#Import Libraries
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from adafruit_motorkit import MotorKit

import sys
import time

#Setup Modbus Connection
client = ModbusClient('localhost',port=5020)
client.connect()
UNIT=0x1        #Address of slave - listen to this address

#Set speed to 0 on init
client.write_register(1,10,unit=UNIT)

#Setup Motor Controller
motor = MotorKit()

#Main Loop
while True:
    rr = client.read_holding_registers(1,1,unit=UNIT)   #Read the register 1 to 1 of this slave
    motor.motor1.throttle = (rr.registers[0]/10)-1      #Set the throttle of the motor (0-20 represents -1 to 1 in increments of 0.1)
    time.sleep(0.1)
