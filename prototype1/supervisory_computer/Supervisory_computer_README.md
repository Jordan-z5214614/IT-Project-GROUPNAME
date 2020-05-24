### Config File

The config file acts as a crucial feature for the setup and deployment of our framework and the current scenario. It allows a user to 
establish how many PLCs they will be running in the scenario and what the login credentials are for these machines. In our current example
system there are two PLCs, that each control a turbine. If a user wants to add more PLCs to control more devices, they only have to update 
the config file to include the additional PLC(s) names and login credentials.


### Supervisory Computer

The supervisory computer as part of the framework, controls the PLCs which will then directly control the devices. This is done through a 
GUI and uses modbus to communicate between devices, in the current scenario, the supervisory computer controls two PLCs. It is also currently set up to be outwards facing on the network, so that the GUI can be run from any computer and used to control the scenario.
