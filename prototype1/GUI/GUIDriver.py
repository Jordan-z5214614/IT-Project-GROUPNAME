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

IP='111.220.27.216'
USER='pi'
PWD='gr0upn@m3'

# ---------------------------------------------------------------- #
# Defines the parameters that can be used by PyQt signal processes
# to send signals outside the main GUI loop
# TODO update these so that parameters are generated dynamically.
# Update will always exist, the others need to be generated.
# ---------------------------------------------------------------- #
class HandlerSignals(Qt.QObject):
    rpm = Qt.pyqtSignal(int)
    update = Qt.pyqtSignal()
    power = Qt.pyqtSignal(int)

# ---------------------------------------------------------------- #
# Handles the back end modbus integration for the GUI app
# ---------------------------------------------------------------- #
class ModbusHandler(Qt.QThread):

    def __init__(self,turbine1,turbine2):
        super(ModbusHandler, self).__init__()

        #Takes the turbines passed and creates local objects
        self.turbine1 = turbine1
        self.turbine2 = turbine2
        #Creates a PLC config dict to take in the SSH info. TODO move this process into parent
        self.plc_configs = {}
        #Create signal handler object
        self.signals = HandlerSignals()
        #Start the modbus local client
        self.startModbusClient()
    #Override deafult PyQt run method
    @Qt.pyqtSlot()
    #Main signal handler loop
    def run(self):
        # ------------------------------------------------------------ #
        # Gets data from only turbine 1 at this stage, then reads/writes
        # to Modbus using the signals, and then calls update to update
        # the GUI, then sleeps
        # ------------------------------------------------------------ #
        while True:
            data = self.turbine1.getValues()
            self.writeModbus(data)
            self.signals.rpm.emit(self.readModbus(2))
            self.signals.power.emit(self.readModbus(1))
            self.signals.update.emit()
            time.sleep(0.01)

    # ---------------------------------------------------------------- #
    # Writes data to the modbus. Bespoke for the demo, TODO need to fix
    # this up to be more generic and compatible
    # ---------------------------------------------------------------- #
    def writeModbus(self,data):

        target=data[2]
        self.client.write_register(0,target,unit=0x01)

    # ---------------------------------------------------------------- #
    # Reads the modbus, and returns the value in the give register
    # TODO parameterise the address as well as the register
    # ---------------------------------------------------------------- #
    def readModbus(self,register):

        registers = self.client.read_holding_registers(register,unit=0x01)
        return(registers.registers[0])

    #Starts the client connection to the Modbus server
    def startModbusClient(self):
        self.client = ModbusClient(IP,5020)
        self.client.connect()

# ------------------------------------------------------------------------------------------ #
# Main GUI class
# Builds a base window that the GUI classes for the different types of devices can be loaded
# onto
# ------------------------------------------------------------------------------------------ #
class GUI:

    plc_config = {}
    func_list = {}

    def __init__(self):
        #starts supervisor and loads PLC configs
        self.startSupervisor()

        #Loads the base window
        self.buildGUI()

        #Loads the threadpool and handlers to process user inputs
        self.threadpool = Qt.QThreadPool()
        handler = ModbusHandler(self.turbine1,self.turbine2)
        handler.signals.rpm.connect(self.turbine1.setRPM)
        handler.signals.power.connect(self.turbine1.setPower)
        handler.signals.update.connect(self.turbine1.update)
        handler.start()

        #Start the GUI loop
        self.window.show()
        self.app.exec_()

        #After the window closes clear Modbus and kill the handler thread
        handler.writeModbus([0,0,0,0,0])
        handler.terminate()

    # ---------------------------------------------------------------- #
    # Starts the supervisor via SSH, and pulls the PLC config files
    # TODO move this to a parent so that the PLC config exists before
    # we try to create the GUI app
    # ---------------------------------------------------------------- #
    def startSupervisor(self):
        #Setup SSH connection
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(IP,username=USER,password=PWD)

        #Setup the config parser
        supervisor_config = configparser.RawConfigParser()

        #Loads the supervisor core config
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat IT-Project-GROUPNAME/prototype1/supervisory_computer/config.txt')
        supervisor_config.read_string(ssh_stdout.read().decode('ascii').strip('\n'))

        for plc in supervisor_config.items('plc list'):
            #Opens the config for the PLC that stored on the Supervisory Computer
            filename = plc[1] + "_config.txt"
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat IT-Project-GROUPNAME/prototype1/supervisory_computer/' + filename)
            config_temp = ssh_stdout.read().decode('ascii').strip('\n')

            #Stores the config in the local dict plc_configs
            self.plc_config.update({plc[0]:config_temp})

        #Starts the supervisor
        ssh.exec_command('python3 IT-Project-GROUPNAME/prototype1/supervisory_computer/supervisorDriver.py')
        time.sleep(5)

        #Close the SSH connection
        ssh.close()

    def buildGUI(self):

        #Setup PyQt window
        self.app = Q.QApplication([])
        self.window = Q.QWidget()

        # ----------------------------------------------------------------- #
        # Creates the windows for each supervisory computer. At this stage,
        # is only set up for a single supervisor and is hard coded.
        # ----------------------------------------------------------------- #
        self.createSupervisorBox("1")

        #Adds supervisor to layout
        layout = Q.QGridLayout()
        layout.addWidget(self.supervisorBox)

        #Adds layout to the window
        self.window.setLayout(layout)

    def createSupervisorBox(self,number):

        #Creates sub-box for supervisory computer
        self.supervisorBox = Q.QGroupBox("Supervisory Computer " + number)

        #Sets up layout
        layout = Q.QGridLayout()

        # ------------------------------------------------------------------ #
        # Creates two turbine objects.
        # TODO - Change the code so this process is dynamic using plc_config
        # ------------------------------------------------------------------ #
        for key, value in plc_config.items():
            for func in value.items('plc function'):
                class_name = func[1]
                func_class = getattr(importlib.import_module(class_name), class_name)
                func_obj = func_class()
                func_key = key + func[0]
                func_list.update({func_key, func_class})

        print(func_list)

        self.turbine1 = Turbine.Turbine()
        self.turbine2 = Turbine.Turbine()

        #Adds created device windows to layout
        layout.addWidget(self.turbine1.createTurbineBox("1"),0,0)
        layout.addWidget(self.turbine2.createTurbineBox("2"),0,1)

        #Adds layout to window
        self.supervisorBox.setLayout(layout)

if __name__=='__main__':

    #Starts the login window
    login = Q.QApplication(sys.argv)
    window = TurbineLogin.Ui()
    login.exec_()

    #Starts the main GUI program
    gui = GUI()
