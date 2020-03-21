# A quick python script to test the
# 8 LED neopixel stick array  

import time
import board
import neopixel


PIN = board.D18
NUM_LED = 8
DELAY = 0.2

pixels = neopixel.NeoPixel(PIN, NUM_LED)

def bar(cycles):
    for i in range(cycles):
        for j in range(NUM_LED):
            pixels[j] = (255,0,0)
            time.sleep(DELAY)
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

# clear all
pixels.fill((0,0,0))

bar(10)

            
        
