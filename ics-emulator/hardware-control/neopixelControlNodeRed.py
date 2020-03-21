
# Neopixel control script for node-red
# Author: Ryan Walsh
# Since: 15/09/19
# Description: User must call program with 4 arguments
# eg. neopixelControlNodeRed.py 0 8 0.01 test
# this example will run the program on RPi pin 10 (MOSI)
# with 8 LEDs using a 0.01s delay (fast lights) using the
# 'test' function

import time
import sys
import board
import neopixel

# All allowed Pins for adafruit NeoPixel library
PIN0 = board.D10    #MOSI
PIN1 = board.D12
PIN2 = board.D18
PIN3 = board.D21
PINS = [PIN0, PIN1, PIN2, PIN3]

# Arguments from node-red
pinSelect = int(sys.argv[1])
numLed = int(sys.argv[2])
delay = float(sys.argv[3])
ledFunc = sys.argv[4]

assert pinSelect >= 0 and pinSelect <=3, "LED Pin selection %r not in range. Only 0..3" % pinSelect
assert numLed >= 0, "Number of LED: %r Must be a positive integer." % numLed
assert delay >= 0, "Delay: %r Must be a positive integer." % delay
assert ledFunc == "test" or ledFunc == "clear" or ledFunc == "normal" or ledFunc == "alarm", "LED function %r does not exist." % ledFunc

pixel = neopixel.NeoPixel(PINS[pinSelect], numLed, pixel_order=neopixel.GRB)

def test(cycles):
    """Tests all LEDs by lighting each pixel
    green in an increasing bar graph
    """
    for i in range(cycles):
        for j in range(numLed):
            pixel[j] = (0,255,0)
            time.sleep(delay)
        # clear all
        pixel.fill((0,0,0))
        time.sleep(delay)

def normal():
    """Green State for all LED"""
    pixel.fill((0,255,0))

def clear():
    """Clear State for all LED"""
    pixel.fill((0,0,0))

def alarm(cycles):
    """Flashes all LED red"""
    for i in range(cycles):
        pixel.fill((255,0,0))
        time.sleep(delay)
        pixel.fill((0,0,0))
        time.sleep(delay)

if (ledFunc == "test"):
        test(2)
elif (ledFunc == "normal"):
        normal()
elif (ledFunc == "clear"):
        clear()
elif (ledFunc == "alarm"):
        alarm(1)
else:
        print("Error. Incorrect function.")
