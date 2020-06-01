### PLC

#### Overview

A PLC(Programmable Logic Controller) or PLU (Programmable Logic Unit) is a small conputer that can be programmed to control low level systems in an ICS. This system uses PLCDriver.py to setup the framework and manage configurations, and PLCLogic.py as a class that users can write their own logic code to handle the connected devices.

#### PLCDriver.py

PLCDriver.py handles the start up of the PLCs, reads the config files, establishes how many devices there will be in the system. It establishes the connection of the PLC to the modbus server, and loads the driver files for each connected device. 

#### Config.txt

Defines the parameters that the PLC needs to operate. Each PLC must have a unique address, and by default should start at 1 and increment. See the supervisory_computer [README](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/prototype1/supervisory_computer/README.md) for more information.

Refer to the commenting within the config file for further information on specific parameters.

#### PLCLogic.py

This file contains the logic for the PLC. It is treated as a class in PLCDriver, and passed 4 arguements, (device_list,param_list,readModbus,writeModbus). 

##### device_list

This is a python dictionary that contains each device listed in the config.txt for this PLC. The key is the device name, and the value is the driver object that was setup using the classfile specified in config.txt. There us further explanation on device drivers below. 

##### param_list

This is a python dictionary that contains the parameter names and addresses as specified in the config.txt for this PLC. The key is the parameter name, and the value is the address. This allows the logic to reflect any changes in config.txt. 

##### writeModbus

This is a python method. It takes two arguments, register and value. Register is the register address to be written, and value is the value to be written. 

##### readModbus

This is a python method. It takes one argument, which is the register to be read. It returns an integer. For more complex modbus operations, i.e. simultaneous register retreval, you can either modify the method in PLCDriver.py, or, write your own method and client for your logic file. 

#### Driver Classes

For each device listed in config.txt, you must define a driver class. This class is made into an object and put in the device_list, meaning the methods in this class will be available for use in the PLCLogic. Multiple devices can share the same driver, as a unique object is created for each device. 
**WARNING** If your device uses GIPO pins which are defined in the driver class, and you wish to use this class for multiple devices this will generate conflicts. Either create multiple class files each with unique pin allocation and define these in the config, or ensure that the pins are only assigned outside the __init__ in a method that takes arguments in PLCLogic. 

#### Current Example 

The PLCs are two Raspberry Pis which control a Lego motor each. Each PLC controls the turbine using Hall Effect sensors to measure the RPM, commands are then given through the PLC to the Lego motor to increase or decrease the RPM, based on user input from the supervisory computer. In the current system configuration, each turbine is controlled by one PLC, even though one PLC is able to control multiple devices, this is done to demonstrate scalability.




