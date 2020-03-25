import sqlite3
from sqlite3 import Error






def writeSensorFeedback(conn, time, output, input):
	cur = conn.cursor()
	cur.execute("INSERT INTO sensorFeedback (timestamp, outputPMWValue, originalInput) VALUES (?, ?, ?)", (time, output, input))

def writeSensorFeedin(conn, date, hour, input):
	cur = conn.cursor()
	cur.execute("INSERT INTO sensorFeedin (currentDate, currentHour, inputPMWValue) VALUES (?, ?, ?)", (date, hour, input))

def writeHMIStoredData(conn, idNum, yourName, user, password, type):
	cur = conn.cursor()
	cur.execute("INSERT INTO HMIStoredData (id, name, userName, PasswordHashed, UserType) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, type))

def writeWCNStoredData(conn, idNum, yourName, user, password, type):
	cur = conn.cursor()
	cur.execute("INSERT INTO WCNStoredData (id, name, userName, PasswordHashed, aliasSystemID) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, alias))

	
	
	
	
	
	

	
	
	
	
def readSensorFeedback(conn):
	try:
    		cur = conn.cursor()
    		cur.execute("SELECT * FROM sensorFeedback")
 
    		rows = cur.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def readSensorFeedin(conn):
	try:
    		cur = conn.cursor()
    		cur.execute("SELECT * FROM sensorFeedin")
 
    		rows = cur.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def readHMIStoredData(conn):
	try:
    		cur = conn.cursor()
    		cur.execute("SELECT * FROM sensorFeedin")
 
    		rows = cur.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def readWCNStoredData(conn):
	try:
    		cur = conn.cursor()
    		cur.execute("SELECT * FROM sensorFeedin")
 
    		rows = cur.fetchall()
 
    		for row in rows:
       			print(row)
			
	except Error as e:
        	print(e)
	
    

	
	
	

	
	
	
	
	
	
	
	
def connect():
	databaseFileLocation = r"C:\sqlite\db\pythonsqlite.db"

    	# creates a database connection
    	conn = createConnection(databaseFileLocation)


    	# read and writes from following tables if there is a connection
    	if conn is not None:

       	 	# inputs data into 
        	createTables(conn, createSensorFeedbackTable)

   	 else:
        	print("The database connection was not established.")

		
		
	

	
	
def main():
	
	databaseFileLocation = r"C:\sqlite\db\pythonsqlite.db"

    	# creates a database connection
    	conn = createConnection(databaseFileLocation)


    	# read and writes from following tables if there is a connection
    	if conn is not None:

       	 	# inputs data into 
        	createTables(conn, createSensorFeedbackTable)
		
		
	
		#Preset test data
	
	

		writeSensorFeedback()
		writeSensorFeedin()
		writeHMIStoredData()
		writeWCNStoredData()
	
	
	
	
	
		readSensorFeedback(conn)
		readSensorFeedin(conn)
		readHMIStoredData(conn)
		readWCNStoredData(conn)
		
		

   	 else:
        	print("The database connection was not established.")

	
	
	
		
		

if __name__ == '__main__':
    main()
