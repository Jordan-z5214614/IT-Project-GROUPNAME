from adafruit_motorkit import MotorKit

class motorDriver():

    motor=MotorKit()

    def setPwm(self,motor_num,input):

        if (motor_num==1):
            motor.motor1.throttle(input)
        elif (motor_num==2):
            motor.motor2.throttle(input)
        elif (motor_num==3):
            motor.motor3.throttle(input)
        elif (motor_num==4):
            motor.motor4.throttle(input)
