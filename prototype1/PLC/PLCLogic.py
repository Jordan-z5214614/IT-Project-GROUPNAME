import time

def main(device_list,param_list,writeModbus,readModbus):

    try:

        writeModbus(int(param_list.get('targetrpm')),0)
        while True:
            time.sleep(0.5)
            targetRPM = readModbus(int(param_list.get('targetrpm')))
            if (targetRPM != 0):
                device_list.get('dev0').setPwm(1,1)
            else:
                device_list.get('dev0').setPwm(1,0)
    except KeyboardInterrupt:
        device_list.get('dev0').setPwm(1,0)
