import sqlite3
from sqlite3 import Error






def writeSensorFeedback(conn, time, output, input):
	try:
		c = conn.cursor()
		c.execute("INSERT INTO sensorFeedback (timestamp, outputPMWValue, originalInput) VALUES (?, ?, ?)", (time, output, input))
	
	except Error as e:
        	print(e)
		
		
def writeSensorFeedin(conn, date, hour, input):
	try:
		c = conn.cursor()
		c.execute("INSERT INTO sensorFeedin (currentDate, currentHour, inputPMWValue) VALUES (?, ?, ?)", (date, hour, input))
	
	except Error as e:
        	print(e)
		
		
def writeHMIStoredData(conn, idNum, yourName, user, password, type):
	try:	
		c = conn.cursor()
		c.execute("INSERT INTO HMIStoredData (id, name, userName, PasswordHashed, UserType) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, type))
		
	except Error as e:
        	print(e)
	
	
def writeWCNStoredData(conn, idNum, yourName, user, password, type):
	try:
		c = conn.cursor()
		c.execute("INSERT INTO WCNStoredData (id, name, userName, PasswordHashed, aliasSystemID) VALUES (?, ?, ?, ?, ?)", (idNum, yourName, user, password, alias))
	
	except Error as e:
        	print(e)
	
	
	
	
	
	

	
	
	
	
def printSensorFeedback(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedback")
 
    		rows = c.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def printSensorFeedin(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def printdHMIStoredData(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		for row in rows:
        		print(row)
			
	except Error as e:
        	print(e)
	
	
	
def printWCNStoredData(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		for row in rows:
       			print(row)
			
	except Error as e:
        	print(e)
	
    

	
	
	
	
	
	
	
	
	
	
	
def readSensorFeedback(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedback")
 
    		rows = c.fetchall()
 
    		return rows
	
	
	
def readSensorFeedin(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		return rows
	
	
	
def readHMIStoredData(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		return rows
	
	
	
def readWCNStoredData(conn):
	try:
    		c = conn.cursor()
    		c.execute("SELECT * FROM sensorFeedin")
 
    		rows = c.fetchall()
 
    		return rows
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def createConnection(databaseFileLocation):

    #create a database connection to the SQLite database specified by databaseFileLocation
    conn = None

    try:
        conn = sqlite3.connect(databaseFileLocation)
        return conn
    except Error as e:
        print(e)

    return conn

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	

	
	
def main():
	
	databaseFileLocation = r"C:\sqlite\db\pythonsqlite.db"

    	# creates a database connection
    	conn = createConnection(databaseFileLocation)


    	# read and writes from following tables if there is a connection
    	if conn is not None:
	
		#Uses Preset test data 
		#TODO change to incoming test data
	

		writeSensorFeedback(conn, 2020-03-28 08:23:12, 1, 2020-03-28 08:23:12)
		writeSensorFeedin(conn, 2020-03-28 08:23:12, 7, -1)
		writeHMIStoredData(conn, 789, smith, john, 2ejnfb3, administration)
		writeWCNStoredData(conn, 34, joe, man, n3end4, administration)
	
	
		printSensorFeedback(conn)
		printSensorFeedin(conn)
		printHMIStoredData(conn)
		printWCNStoredData(conn)
		
		readSensorFeedback(conn)
		readSensorFeedin(conn)
		readHMIStoredData(conn)
		readWCNStoredData(conn)
		
		

   	 else:
        	print("The database connection was not established.")

	
	
	
		
		

if __name__ == '__main__':
    main()
