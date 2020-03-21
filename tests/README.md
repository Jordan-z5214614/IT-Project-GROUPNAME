# Testing

This directory holds the testing files associated with this project. 

## Hardware
### Functional Testing
Please use the functional test script in the same directory as the hardware python programs (its in there as well). 
The intention of this script is to allow the user to run this script and easily identify the ports and pins for the relevant motors and LED hoocked up to the Raspbery Pi and Hat.

### Feasiblity Testing.
This is to ensure the hardware is fit for purpose can be achieved now using the inbuit hardware programs, the methodolgy used is to build and construct the hardware, then ensure that it performs as expected. As an example, when selecting motors for the wind turbine scenario, we needed to satisfy the contraint that the motor will be able to power the turbine at 20RPM safely. We had originally thought this could be acheived using special PWM control, but the feasibility testing proved this was not the case. To test the motors, a low and high point of reference was measure by PWM control. The lower constraint was how low the motor could be powered using PWM before it was overcome with friction and gravity forces, stalling out. High was tested as 100% PWM. 