#!/usr/bin/env python3

import PyQt5.QtWidgets as Q
import PyQt5.QtCore as Qt
import TurbineLogin
import Turbine
import sys
import paramiko
import time
import multiprocessing
import configparser
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
class HandlerSignals(Qt.QObject):
    rpm = Qt.pyqtSignal(int)
    update = Qt.pyqtSignal()
    power = Qt.pyqtSignal(int)
class ModbusHandler(Qt.QThread):
    IP='111.220.27.216'
    USER='pi'
    PWD='gr0upn@m3'

    def __init__(self,turbine1,turbine2):
        super(ModbusHandler, self).__init__()
        self.turbine1 = turbine1
        self.turbine2 = turbine2
        self.plc_configs = {}
        self.signals = HandlerSignals()
        self.startSupervisor()
        self.startModbusClient()
    @Qt.pyqtSlot()
    def run(self):
        while True:
            data = self.turbine1.getValues()
            self.writeModbus(data)
            self.signals.rpm.emit(self.readModbus(2))
            self.signals.power.emit(self.readModbus(1))
            self.signals.update.emit()
            time.sleep(0.01)

    def writeModbus(self,data):

        target=data[2]
        self.client.write_register(0,target,unit=0x01)

    def readModbus(self,register):

        registers = self.client.read_holding_registers(register,unit=0x01)
        return(registers.registers[0])

    def startSupervisor(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.IP,username=self.USER,password=self.PWD)

        supervisor_config = configparser.RawConfigParser()

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat IT-Project-GROUPNAME/prototype1/supervisory_computer/config.txt')
        supervisor_config.read_string(ssh_stdout.read().decode('ascii').strip('\n'))
        for plc in supervisor_config.items('plc list'):
            #Opens the config for the PLC that stored on the Supervisory Computer
            filename = plc[1] + "_config.txt"
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat IT-Project-GROUPNAME/prototype1/supervisory_computer/' + filename)
            plc_config = ssh_stdout.read().decode('ascii').strip('\n')

            self.plc_configs.update({plc[1]:plc_config})

        print(self.plc_configs)
        #Starts the supervisor
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
        handler.signals.rpm.connect(self.turbine1.setRPM)
        handler.signals.power.connect(self.turbine1.setPower)
        handler.signals.update.connect(self.turbine1.update)
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
    login = Q.QApplication(sys.argv)
    window = TurbineLogin.Ui()
    login.exec_()
    gui = GUI()
