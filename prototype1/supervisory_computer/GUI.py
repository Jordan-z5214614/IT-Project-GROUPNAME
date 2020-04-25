import time
import sys
import threading

targetRPM=0
def get_target():
    while True:
        targetRPM=input()

def main(plc_list,client,writeModbus,readModbus):

    global targetRPM

    plc1_address = list(plc_list.get('plc1').keys())[0]
    targetRPM_reg = int(plc_list.get('plc1').get(plc1_address).get('targetrpm'))
    PWM_reg = int(plc_list.get('plc1').get(plc1_address).get('pwm'))
    RPM_reg = int(plc_list.get('plc1').get(plc1_address).get('rpm'))

    try:
        while True:

            targetRPM = int(input("Enter RPM "))
            writeModbus(targetRPM_reg,targetRPM,0x00)
            print("RPM set to " + str(readModbus(targetRPM_reg,0x00)))
            print("Current RPM " + str(readModbus(RPM_reg,0x00)))
            time.sleep(0.5)
    except KeyboardInterrupt: raise
