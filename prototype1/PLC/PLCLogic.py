def main(device_list,param_list,writeModbus,readModbus):
    device_list['dev0'].setPwm("test")
    print(device_list['dev1'].getRpm())
