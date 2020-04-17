import time
import sys
import logging

def main(device_list,param_list,writeModbus,readModbus):
    logf = open("logic.log","w")
    try:
        PWM = 0
        writeModbus(3,0)
        motor = device_list.get('dev0')
        sens = device_list.get('dev1')
        while True:
            time.sleep(0.001)
            targetRPM = readModbus(int(param_list.get('targetrpm')))
            RPM = sens.getRPM()
            if (targetRPM == 0):
                PWM = 0
                motor.setPwm(1,PWM)
                sens.resetRPM()
            elif (targetRPM > RPM and PWM < 1000):
                PWM = PWM + 1
                motor.setPwm(1,(PWM/1000))
            elif (targetRPM < RPM and  PWM > 0):
                PWM = PWM - 1
                motor.setPwm(1,PWM/1000)

            writeModbus(int(param_list.get('rpm')),RPM)
            writeModbus(int(param_list.get('pwm')),PWM)
    except Exception as e:
        device_list.get('dev0').setPwm(1,0)
        writeModbus(3,1)
        logf.write("Error {0}:\n".format(str(e)))
