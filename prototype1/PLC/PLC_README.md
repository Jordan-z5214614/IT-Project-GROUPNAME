### PLC

The PLCs are two Raspberry Pis which control a Lego motor each. Each PLC controls the turbine using Hall Effect sensors to measure the RPM, commands are then given through the PLC to the Lego motor to increase or decrease the RPM, based on user input from the supervisory computer. In our framework for PLCs, there should be a PLC (in this case Raspberyy Pi) for each device, rather than one PLC controlling multiple devices.


### PLCDriver.py

PLCDriver. py handles the start up of the PLCs, by reading the config file, to establish how many PLCs and devices there will be in the system. It establishes the connection of the PLCs, devices and the Modfbus client.

