#!/usr/bin/env python3
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from multiprocessing import Process
import modbusServer
import sys
import time

def main():

    server = Process(target=modbusServer.run_server)

    try:
        server.start()

        client = ModbusClient('localhost',5020)
        client.connect()

        while True:
            pwm = input("Enter PWM: ")
            client.write_register(0,int(pwm),unit=0)

    except KeyboardInterrupt:
        print("Shutting down")
        server.terminate()



if __name__ == "__main__":

    main()
