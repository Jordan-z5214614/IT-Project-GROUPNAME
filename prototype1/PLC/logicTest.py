import speedSensDriver
import motorDriver
import time 
import sys

def main():
    targetRPM = 400
    PWM = 0

    try:

        motor = motorDriver.motorDriver()
        speed = speedSensDriver.speedSensDriver()

        while True:

            RPM = speed.getRPM()

            if (RPM < targetRPM and PWM < 999):
                PWM = PWM + 1
            elif (RPM > targetRPM and PWM > 0):
                PWM = PWM - 1
            motor.setPwm(1,PWM/1000)
            sys.stdout.write("\rRPM: " + str(RPM) + " PWM: " + str(PWM))
            sys.stdout.flush
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Bye")
        motor.setPwm(1,0)
if __name__=='__main__':
    main()
