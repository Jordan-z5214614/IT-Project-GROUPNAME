# Motor Controller Script
# Author: Ryan Walsh
# Since 15/09/19

import time
import sys
from adafruit_motorkit import MotorKit

# Common variables
DELAY = 1
MOTORHAT_ADDR = [0x60, 0x61, 0x62, 0x63, 0x64] # predefined I2C addresses for each HAT in stack starting at 0x60 

# Motor Hat Variables
try:
    motorHatNum = int(sys.argv[1]) # motor hat to address
    motorNum = int(sys.argv[2]) # motor port on hat (eg. m1=1, m2=2)
    speed = float(sys.argv[3]) # float percentage of full PWN speed eg 0.1 = 10%
except TypeError:
    print ("Argument is of the wrong type\n")
else:
    # User input assertions
    assert (motorHatNum >= 0 and motorHatNum <= 4),"MotorHat address out of range. 0..4 only"
    assert (motorNum >= 1 and motorHatNum <= 4),"MotorNum out of range. 1..4 only"
    assert (speed >= 0 and motorHatNum <= 1),"Speed out of range. 0-1 only"

    # init hat and motor
    hat = MotorKit(address = MOTORHAT_ADDR[motorHatNum])

    # Assume speed is 0-1 only, where 0 means no power to motor
    if speed <= 0:
        speed == None # allows motor to 'coast' instead of induce braking forces

    # run motor number as indicated on Hat DC motor ports
    if motorNum == 1:
        hat.motor1.throttle = speed
    elif motorNum == 2:
        hat.motor2.throttle = speed
    elif motorNum == 3:
        hat.motor3.throttle = speed
    elif motorNum == 4:
        hat.motor4.throttle = speed
    else:
        print("Error. Motor Number out of bounds.")
