#!/usr/bin/env python3
#TODO Flesh out user inputs. Configure to take registers/addresses from a config file

#Import modbus protocol 
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#Import modbus server driver
import modbusServer
#Import python libs
from multiprocessing import Process
import paramiko
import configparser
import sys
import time

#Connects using SSH and launches PLCDriver on the passed PLC unit
def plc_start(hostname,username,password):

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=hostname,username=username,password=password)
    ssh_stdin = ssh.exec_command('./IT-Project-GROUPNAME/prototype1/PLC/PLCDriver.py')

#Starts a server in a thread, then takes a PWM value from the user. 
def main():

    server = Process(target=modbusServer.run_server)

    #Read in config file
    config = configparser.RawConfigParser()
    file = r'config.txt'
    config.read(file)


    try:
        server.start()

        for plc in config.items('plc list'):

            username = config.get(plc[0],'username')
            password = config.get(plc[0],'password')
            hostname = plc[1]

            plc_start(hostname,username,password)

        client = ModbusClient('supevisor',5020)
        client.connect()

        while True:
            pwm = input("Enter PWM: ")
            client.write_register(0,int(pwm),unit=0) #register address and device address are hard coded for testing. Will be dynamic from config file in end product

    except KeyboardInterrupt:
        print("\nShutting down")
        server.terminate()



if __name__ == "__main__":

    main()
