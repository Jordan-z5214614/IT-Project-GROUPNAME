#!/usr/bin/env python3

import write.py as write
import time

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusCliebt("localhost", port=5020)
client.connect()
UNIT=0x01

con = write.createConnection("./db/log.db")

while True:

    rr = client.read_holding_registers(1,1,unit=UNIT)
    pwm = registers[0]

    time = time.strftime("%Y%m%d%H%M%S",time.localtime()) 
    write.sensorFeedback(con,time,pwm)

    time.sleep(1)
