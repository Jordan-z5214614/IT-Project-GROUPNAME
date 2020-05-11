#!/usr/bin/env python3

import PyQt5.QtWidgets as Q
import PyQt5.QtCore as Qt
import Turbine
import paramiko
import time
import multiprocessing
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

class ModbusHandler(Qt.QThread):
    IP='192.168.1.104'
    USER='pi'
    PWD='gr0upn@m3'

    def __init__(self,turbine1,turbine2):
        super(ModbusHandler, self).__init__()
        self.turbine1 = turbine1
        self.turbine2 = turbine2

        self.startSupervisor()
        self.startModbusClient()
    @Qt.pyqtSlot()
    def run(self):
        while True:
            data = self.turbine1.getValues()
            self.writeModbus(data)
            self.turbine1.RPM = self.readModbus()
            self.turbine1.update()

    def writeModbus(self,data):

        target=data[2]
        self.client.write_register(0,target,unit=0x00)

    def readModbus(self):

        registers = self.client.read_holding_registers(2,unit=0x00)
        return(registers.registers[0])

    def startSupervisor(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.IP,username=self.USER,password=self.PWD)

        ssh.exec_command('python3 IT-Project-GROUPNAME/prototype1/supervisory_computer/supervisorDriver.py')
        time.sleep(5)

        ssh.close()

    def startModbusClient(self):
        self.client = ModbusClient(self.IP,5020)
        self.client.connect()
class GUI:

    
    def __init__(self):
        self.buildGUI()
        self.threadpool = Qt.QThreadPool()
        handler = ModbusHandler(self.turbine1,self.turbine2)
        handler.start()
        self.window.show()
        self.app.exec_()
        handler.writeModbus([0,0,0,0,0])
        handler.terminate()
    def buildGUI(self):
        self.app = Q.QApplication([])
        self.window = Q.QWidget()

        self.createSupervisorBox("1")

        layout = Q.QGridLayout()
        layout.addWidget(self.supervisorBox)

        self.window.setLayout(layout)

    def createSupervisorBox(self,number):
        self.supervisorBox = Q.QGroupBox("Supervisory Computer " + number)

        layout = Q.QGridLayout()
        self.turbine1 = Turbine.Turbine()
        layout.addWidget(self.turbine1.createTurbineBox("1"),0,0)
        self.turbine2 = Turbine.Turbine()
        layout.addWidget(self.turbine2.createTurbineBox("2"),0,1)

        self.supervisorBox.setLayout(layout)

if __name__=='__main__':
    gui = GUI()
