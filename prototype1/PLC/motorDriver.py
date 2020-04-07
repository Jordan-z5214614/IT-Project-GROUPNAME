from adafruit_motorkit import MotorKit

class motorDriver():

    def __init__(self):

        self.motor=MotorKit()

    def setPwm(self,motor_num,input):

        if (motor_num==1):
            self.motor.motor1.throttle = input
        elif (motor_num==2):
            self.motor.motor2.throttle = input
        elif (motor_num==3):
            self.motor.motor3.throttle = input
        elif (motor_num==4):
            self.motor.motor4.throttle = input
