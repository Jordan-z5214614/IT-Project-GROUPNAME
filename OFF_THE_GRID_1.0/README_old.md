# OFF THE GRID 
A Cyber-Physical Emulation System for Scenario-Based Training

[For a full guide see our WIKI](https://github.com/Mikaela199/IT-Project-2/wiki)

## Intro
This repo will hold the University project 'Off The Grid', A Cyber-Physical Emulation System for Scenario-Based Training. 
The system will provide a means to run scenarios that emulate Cyber-Physical Systems to be accessed for a small group of students to interact with as attackers. 

## System Components
### GUI
The GUI will provide course conveners the means to easily deploy, configure, observe and maintain the CPS scenarios of the system.
### ICS Components
#### Modbus emulator
Node red will be utilised as the main platform for building the ICS components, utlising the Modbus package and various flows to emulate complex CPS components. This will all be run from a set of raspberry pi in a client server relationship.
#### Historian
A SQL server will be configured in a vulnerable manner to provide an attack path for the system
### Hardware
A detailed physical system that takes inputs from the emulated system to provide visual and kinetic effects in a scale model. Utilising the GPIO pins on the Raspberry Pi to communicate with Adafruit Neopixel LED strips and DC motors using the Adafruit motor control hat.

## Prerequisites
You must have the following installed on the Raspberry Pi to be used for running the system:
* node.js
* npm
* node-red
* node-red-contrib-modbus
* node-red-dashboard
* node-red-contrib-aggregator
* python3
* python3-dev
* pip3
* adafruit-circuitpython-neopixel
* adafruit-circuitpython-motorkit
* Docker

See the wiki page for a [Full Guide](https://github.com/Mikaela199/IT-Project-2/wiki/).
