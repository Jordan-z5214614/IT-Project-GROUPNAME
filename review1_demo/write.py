import sqlite3
from sqlite3 import Error



def writeSensorFeedback(time, output, input):
	connect()
	cur.execute("INSERT INTO sensorFeedback (timestamp, outputPMWValue, originalInput) VALUES (?, ?, ?)", (time, output, input))

def writeSensorFeedin(date, hour, input)
	connect()
	cur.execute("INSERT INTO sensorFeedin (currentDate, currentHour, inputPMWValue) VALUES (?, ?, ?)", (date, hour, input))

def writeHMIStoredData(idNum, yourName, user, password, type)
	connect()
	cur.execute("INSERT INTO HMIStoredData (id, name, userName, PasswordHashed, UserType) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, type))

def writeWCNStoredData(idNum, yourName, user, password, type)
	connect()
	cur.execute("INSERT INTO WCNStoredData (id, name, userName, PasswordHashed, aliasSystemID) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, alias))






def connect()
	database = r"C:\sqlite\db\pythonsqlite.db"

    	# creates a database connection
    	conn = createConnection(databaseFileLocation)


    	# read and writes from following tables if there is a connection
    	if conn is not None:

       	 	# inputs data into 
        	createTables(conn, createSensorFeedbackTable)

   	 else:
        	print("The database connection was not established.")


if __name__ == '__main__':
    main()