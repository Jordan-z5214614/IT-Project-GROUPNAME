# Simulated Industrial Control System Hacking Scenario
## A Cyber-Physical Emulation System for Scenario-Based Training

Developed by: $GROUPNAME

![alt text](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/Images%20of%20the%20Parts%20for%20the%20Project/Logo_Design.png)

# Introduction
This repo will hold the University project 'Off The Grid', A Cyber-Physical Emulation System for Scenario-Based Training. 
The system will provide a means to run scenarios that emulate Cyber-Physical Systems to be accessed for a small group of students to interact with as attackers. 

### Aim:

The project aims to allow for a modular framework to enable future ICS simulated hacking scenarios to be built. We have developed a functioning simulated scenario for controlling a powerplant turbine in an industrial control system. We have also created a scenario, using this framework, which emulates a turbine from a nuclear power plant. These scenarios aim to educate and facilitate honing Cyber-Security skills in an Industrial Control System (ICS) context. 

Features supported by this system:
- Hacking a simulated powerplant turbine
- Defining your own scenario
- Creating added systems

### History:

This project expands upon a prototype platform for teaching the hacking of cyber-physical systems (such as power grid devices, traffic lights, and critical infrastructure). The current ICS hacking range in use by UNSW has a running cost too high to facilitate its regular use as a teaching resource, however, it uses the real software and hardware of industrial ICS. UNSW is seeking a more cost-effective solution which does not use the real software or hardware. A previous attempt to create a similar scenario was the construction of a wind power turbine, controlled by ICS. This previous project will be built on. 

[For a full guide see the past projects WIKI](https://github.com/Mikaela199/IT-Project-2/wiki)




# System Components:

- GUI:
The GUI will provide as another attack path for the system. The GUI will give access to be able to change variables of the turbine.
- Modbus emulator:
Pymodbus will be utilised as the main platform for building the ICS components. This will all be run from a set of Raspberry Pi's.
- Database Logger:
A SQL server will be configured in a vulnerable manner to provide an attack path for the system. This sends alerts to the system of unusual behaviour.
- Sensors:
Virtual sensors will be configured to add another attack vector for the system.
- Hardware:
A detailed physical system that takes inputs from the emulated system to provide visual and kinetic effects in a scale model of a power plants turbine. Utilising the GPIO pins on the Raspberry Pi to communicate with DC motors using the Adafruit motor control hat. 





# QuickStart


 ### Physical Requirements:
 - Raspberry Pi 4 x3
 - Raspberry Pi's HDMI connector x3
 - Raspberry Pi's power supply x3
 - SD cards containing micro SD card x3
 - mouse 
 - keyboard
 - Laptop or PC with SD card port
 - Raspberry Pi HATs x2
(We used the Adafruit motor control HATs from the "Adafruit DC & Stepper Motor HAT for Raspberry Pi - Mini Kit". This can be brought from the following link: https://www.adafruit.com/product/2348)

![alt text](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/Images%20of%20the%20Parts%20for%20the%20Project/Raspberry-Pi-Hat.JPG)

![alt text](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/Images%20of%20the%20Parts%20for%20the%20Project/Raspberry-Pi-Hat-in-Use.JPG)

 - lego motor x2
(We used the motor from the LEGO® Power Functions medium motor and 2 19.6” (50cm) extension wires, officially titled as the "LEGO® Power Functions M-Motor". This can be brought from the following link: https://www.lego.com/en-us/product/lego-power-functions-m-motor-8883)

![alt text](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/Images%20of%20the%20Parts%20for%20the%20Project/Lego-Motor.JPG)

![alt text](https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/Images%20of%20the%20Parts%20for%20the%20Project/Lego-Motor-in-Use.JPG)

 - turbine pieces x2 #TODO change to be open "can really be anything that connects to the motor
 - appropriate connectors and pieces (see diagram below for full picture)
 - Lego power plant station (optional please view the Lego Design folder for more details)
 
### Set Up:

Use the "HOW TO SET UP RASPBERRY PI'S" document for the initial set up your Raspberry Pi's or follow the tutorial on https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/4 
 
After the setup has been completed install the requirements listed in the "requirements.txt" from the link or from the master above:
https://github.com/Jordan-z5214614/IT-Project-GROUPNAME/blob/master/requirements.txt

These are also listed below for your convienance:



After all the Raspberry Pi's have the requirements installed, the Raspberry Pi's can be set up. 

1) Install all the files in the Supervisory Computer onto 1 Raspberry Pi. Then run the Driver file.
2) On the the last two Rasperry Pi's install all the files in the PLC files on each Raspberry Pi. Then run the Drvier file.




 
