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
    print(plc1_address)
    try:
        while True:

            targetRPM = int(input("Enter RPM "))
            writeModbus(targetRPM_reg,targetRPM,plc1_address)
            print("RPM set to " + str(readModbus(targetRPM_reg,plc1_address)))
            print("Current RPM " + str(readModbus(RPM_reg,plc1_address)))
            #print(str(readModbus(targetRPM_reg,plc1_address)))
            print(str(readModbus(targetRPM_reg,'0x01')))
            print(str(readModbus(targetRPM_reg,'0x02')))
    except KeyboardInterrupt: raise
