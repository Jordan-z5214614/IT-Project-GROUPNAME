#!/usr/bin/env python3

#Import Libraries
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sqlite3
from sqlite3 import Error
from datetime import datetime
import time

#Writes a value to the database
def writeSensorFeedback(con, time, output):

    try:
        c = con.cursor()	#Sets the cursor
        c.execute("INSERT INTO sensorFeedback (timestamp, outputPWMValue) VALUES (?, ?)", (time, output))	#SQL query
        con.commit()	#commit changes

    except Error as e:
        print(e)

#Main program
def main():

    #Sets up modbus connection
    client = ModbusClient("localhost", port=5020)
    client.connect()
    UNIT=0x01 #Slave address were recording for

    con = sqlite3.connect("./db/log.db")	#Database location

    #Main loop
    while True:

        rr = client.read_holding_registers(1,1,unit=UNIT) 	#Get register 1 values
        pwm = (rr.registers[0]/10)-1				#Convert to -1 - 1 format

        time_now = datetime.now().strftime("%y%m%d%H%M%S.%f")	#Gets time now
        writeSensorFeedback(con,time_now,pwm)				#Write to db

        time.sleep(0.5)							#Wait 1/2 second


if __name__ == '__main__':
    main()
