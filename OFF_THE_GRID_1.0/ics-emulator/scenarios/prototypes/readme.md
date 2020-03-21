# Prototyping Notes

Spent a while trying to create a node-red node using some established npm packages, 
however they are outdated and have 6 critical dependency issues.

So I have ventured into a more baremetal approach, either create a whole new node.js for a python based system or use python directly in node-red.
Python was the obvious choice.
Using the adafruit motor hat and the adafruit neopixels for the raspberry pi, we are using established libraries that are actively maintained by adafruit

## Neopixel Control
There are a few things to note, for neopixel control, adafruit/raspberry pi support 4 individual GPIO pins for neopixel data out. 
In BCM format: 
- 10 (MOSI)
- 12
- 18
- 21
The neopixel native control does not allow multiple pins to be controlled at once, the proposed code we will develop will be able to control 
multiple PIN outs in node-red.

**Source:**

https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel

https://github.com/adafruit/Adafruit_Blinka/blob/master/src/adafruit_blinka/microcontroller/bcm283x/neopixel.py


## Motor Control
Although there is a npm package motor-hat, many dependencies are outdated and the package is not looked after. Therefore to fully utilise the 
motor hat we will also use adafruits python libraries directly.

**Source:**

https://github.com/adafruit/Adafruit_CircuitPython_MotorKit

