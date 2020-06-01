### Config File

Each config file, is independent for each device. The config file acts as a crucial feature for the setup and deployment of our framework and the current scenario. It allows a user to establish how many PLCs they will be running in the scenario and what the login credentials are for these machines. In our current example system there are two PLCs, that each control a turbine. If a user wants to add more PLCs to control more devices, they only have to update the config file to include the additional PLC(s) names and login credentials.


### Supervisory Computer

The supervisory computer as part of the framework. It handles the Modbus Server, and handles setting up and starting the framework. In the current scenario, the supervisory computer connects to two PLCs, and loads the relevant config files.

To launch the scenario, supervisorDriver.py must be executed. This starts the server in modbusServer.py. This is already done if using the standard GUI package, but bespoke applications may require it to be called manually to run the scenario. The driver then connects to each PLC listed in the its config file, and retrieves their config files which are saved locally. 

It is currently set up to be outwards facing on the network, so that the GUI can be run from any computer and used to control the scenario, however the GUI could also be run directly on the supervisor. In this instance, the full version of rapian must be loaded (not headless), or, alternativley, a command line GUI could be implemented. 

### Modbus Server

The server is an implementation of the pymodbus package. It is configured by default to use the standard TCP protocol, with the standard TCP framer. Refer to the pymodbus documentation [here](https://pymodbus.readthedocs.io/en/latest/source/example/synchronous_server.html). 

#### Slave Addresses

The default run_server() method has been modified to accept an integer, which is the number of slave devices (in this context PLCs) to initialise and assign addresses. By default, the addresses are assigned incrementally, starting at 1. If you desire to use non sequential addresses, modify the slaves.update method call (again, refer to the pymodbus documentation for further information)

#### Port and domain

The server is configured to be internet facing and run on port 5020 (0.0.0.0,5020) using the StartTcpServer() method. You can modify this to whatever values you require, as long as the server details in PLC/config.txt are updated for each device accordingly. The method accepts 'localhost' as a domain. 

### Modifiying the supervisor

The supervisor was designed to be relativley easy to modify to suit bespoke applications. You can launch your own class (or code) in the main method, and even pass a modbus client object so that the program can read/write to the bus. 
