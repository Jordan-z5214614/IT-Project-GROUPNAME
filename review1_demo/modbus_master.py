#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import time
import sys

client = ModbusClient('localhost', port=5020)
UNIT=0x1

client.connect()

while True:
    client.write_coil(1, True, unit=UNIT)
    time.sleep(1)
    client.write_coil(1, False, unit=UNIT)
    time.sleep(1)
