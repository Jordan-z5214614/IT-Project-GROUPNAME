
import time
import math
import datetime
import RPi.GPIO as GPIO


pulse = 0
elapsed_time = 0
start_time = time.time()
class speedSensDriver():


    def calcInterval(self,channel):

        global pulse, start_time, elapsed_time

        pulse += 1
        elapsed_time = time.time() - start_time
        start_time = time.time()

    def getRPM(self):

        global pulse, elapsed_time
        if (elapsed_time != 0):
            return(int((1/elapsed_time*60)/2))
        else:
            return(0)
    def resetRPM(self):

        global elapsed_time, start_time

        elapsed_time = 0
        start_time = time.time()
    def getPulse(self):
        return(pulse)
    def getTime(self):
        return(elapsed_time)
    def __init__(self):

        GPIO.cleanup()

        # Tell GPIO library to use GPIO references
        GPIO.setmode(GPIO.BCM)

        # Set Switch GPIO as input
        # Pull high by default
        GPIO.setup(21 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(21, GPIO.FALLING, callback=self.calcInterval, bouncetime=20)
