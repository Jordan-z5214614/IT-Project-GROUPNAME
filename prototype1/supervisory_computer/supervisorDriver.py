#!/usr/bin/env python3
#TODO Flesh out user inputs. Configure to take registers/addresses from a config file

#Import modbus server from pymodbus
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

#Import python libs
from multiprocessing import Process
import modbusServer
import sys
import time

#Starts a server in a thread, then takes a PWM value from the user. 
def main():

    server = Process(target=modbusServer.run_server)

    try:
        server.start()

        client = ModbusClient('supevisor',5020)
        client.connect()

        while True:
            pwm = input("Enter PWM: ")
            client.write_register(0,int(pwm),unit=0) #register address and device address are hard coded for testing. Will be dynamic from config file in end product

    except KeyboardInterrupt:
        print("Shutting down")
        server.terminate()



if __name__ == "__main__":

    main()
