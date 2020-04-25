import time
import sys
import GUI

class supervisorInterface():



    def writeModbus(self,register,value,address):
        self.client.write_register(register,value,unit=address)
    def readModbus(self,register,address):
        registers = self.client.read_holding_registers(register,unit=address)
        return(registers.registers[0])

    def __init__(self,plc_list,client):
        self.client = client
        try:
            GUI.main(plc_list,client,self.writeModbus,self.readModbus)
        except KeyboardInterrupt: raise
