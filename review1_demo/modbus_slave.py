#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('localhost',port=5020)
client.connect()
UNIT=0x1
import time
import sys
while True:
    rr = client.read_coils(1,1,unit=UNIT)
    result = rr.bits[0]
    sys.stdout.write("\rOutput: %s" % result)
    time.sleep(1)
    sys.stdout.flush()
    rr = client.read_coils(1,1,unit=UNIT)
    result = rr.bits[0]
    sys.stdout.write("\routput: %s" % result)
    time.sleep(1)
    sys.stdout.flush()
