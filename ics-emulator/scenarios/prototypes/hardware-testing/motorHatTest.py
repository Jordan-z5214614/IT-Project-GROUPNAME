# Full motor hat test for OTG
# Author: Ryan Walsh
# Since 13/09/19

import time
import board
import neopixel
from adafruit_motorkit import MotorKit


PIN = board.D18
NUM_LED = 8
DELAY = 1

pixels = neopixel.NeoPixel(PIN, NUM_LED)
kit = MotorKit()

kit.motor1.throttle = 0

def bar(cycles):
    for i in range(cycles):
        for j in range(NUM_LED):
            kit.motor2.throttle = (j/NUM_LED) # run motor at bar graph percentage
            pixels[j] = (255,0,0)
            time.sleep(DELAY)
            kit.motor2.throttle = 0 # stop motor
        # clear all
        pixels.fill((0,0,0))
        time.sleep(DELAY)


# fill all red
pixels.fill((255,0,0))

time.sleep(DELAY)

# fill all green
pixels.fill((0,255,0))

time.sleep(DELAY)

# fill all blue
pixels.fill((0,0,255))

time.sleep(DELAY)
bar(5)