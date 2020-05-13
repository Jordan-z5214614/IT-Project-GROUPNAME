#!/usr/bin/env python3

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
import supervisorInterface

#Connects to the targeted PLC, retrieves the config file and then starts the PLCDriver process on that device
def plc_start(hostname,username,password):

    #Sets up ssh connection
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname,username=username,password=password)

    #Retrieves config file and stores in plc_config
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat IT-Project-GROUPNAME/prototype1/PLC/config.txt')
    plc_config = ssh_stdout.read().decode('ascii').strip('\n')

    #Starts the PLCDriver process on remote device
    ssh.exec_command('python3 IT-Project-GROUPNAME/prototype1/PLC/PLCDriver.py')

    #Closes the SSH connection
    ssh.close()

    return(plc_config)

#For each PLC listed in the supevisor config file, calls plc_start on each and saves the PLCs individual config data in plc_list. 
#The config data saved is PLC Modbus Address, and the assosiated parameters and their respective modbus register addresses. 
#The format is dict<String name, dict<String address, dict<String Parameter Name, Int Register Number>>>
def load_plcs():

    plc_list = {}

    #Read in supevisor config file
    config = configparser.RawConfigParser()

    file = r'/home/pi/IT-Project-GROUPNAME/prototype1/supervisory_computer/config.txt'
    config.read(file)

    #Iterates the PLCs listed in the supevisor config file
    for plc in config.items('plc list'):

        print("Connecting to " + plc[0] + "... ", end='')
        #Loads PLC login creds. #TODO configure to use SSH Keys instead
        username = config.get(plc[0],'username')
        password = config.get(plc[0],'password')
        hostname = plc[1]

        #Setup configparser object to store PLC config data
        plc_config = configparser.RawConfigParser()

        #Call plc_start and save config data
        plc_config.read_string(plc_start(hostname,username,password))

        param_list = {}

        #Save parameter list in PLCs config file
        param_list.update(plc_config.items('parameter addresses'))

        #Store PLC address and parameter list in plc_list
        plc_list.update({plc[0]:{plc_config.get('address','address'):param_list}})

        print("Done!")
    return(plc_list)

#Starts a server in a thread, then takes a PWM value from the user. 
def main():

    server = Process(target=modbusServer.run_server)

    try:
        print("Starting Modbus Server...", end='')
        server.start()
        print("Done!")

        print("Starting PLCs...", end='')
        plc_list = load_plcs()
        print("Done!")

        print("Starting user interface...")
        client = ModbusClient('supevisor',5020)
        client.connect()

        #interface = supervisorInterface.supervisorInterface(plc_list,client)


    except KeyboardInterrupt:
        print("\nShutting down")
        server.terminate()
        client.close()

if __name__ == "__main__":

    main()
