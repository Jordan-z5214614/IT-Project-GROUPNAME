import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# range init
low = 8
high = 30

# PWM init
dc = 0
f = 50

# Motor Pins using BCM
M1_EN1 = 18 # Speed Control Pin
M1_IN1 = 17 # Direction Control Pin
M1_IN2 = 27 # Direction Control Pin


GPIO.setup(M1_EN1, GPIO.OUT)
GPIO.setup(M1_IN1, GPIO.OUT)
GPIO.setup(M1_IN2, GPIO.OUT)

pwm = GPIO.PWM(M1_EN1, f) # 50Hz PWM
pwm.start(dc) # duty cycles 

# FWD
GPIO.output(M1_IN1, GPIO.HIGH)
GPIO.output(M1_IN2, GPIO.LOW)

# increase PWM to accelerate/decelerate motor
# this tracks the lowest PWM for low speed control
try:
    while 1:
        for dc in range(low, high, 1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(3)
            print "Test dc: ", dc
        for dc in range(high, low, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(3)
            print "Test dc: ", dc
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()



