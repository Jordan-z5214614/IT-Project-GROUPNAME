#References:
#
#
#


import sqlite3
from sqlite3 import Error




def createConnection(databaseFileLocation):

    #create a database connection to the SQLite database specified by databaseFileLocation
    conn = None

    try:
        conn = sqlite3.connect(databaseFileLocation)
        return conn
    except Error as e:
        print(e)

    return conn





def createTables(conn, createGivenTable):

    try:
        c = conn.cursor()
        c.execute(createGivenTable)

    except Error as e:
        print(e)






def main():
    database = r"C:\sqlite\db\pythonsqlite.db"




     createSensorFeedbackTable = """ CREATE TABLE IF NOT EXISTS sensorFeedback (
                                        timestamp datetime NOT NULL UNIQUE PRIMARY KEY,
                                        outputValue int,
					dutyCycle int,
					FOREIGN KEY(originalInput) REFERENCES sensorFeedin(datetime)
					
                                    ); """
	


    createSensorFeedinTable = """ CREATE TABLE IF NOT EXISTS sensorFeedin (
                                        currentDate date  NOT NULL UNIQUE PRIMARY KEY,
					currentHour int NOT NULL PRIMARY KEY,
                                        dutyCycle int,
					inputValue int

                                    ); """
	




    createHMITable = """CREATE TABLE IF NOT EXISTS HMIStoredData (
                                    id integer PRIMARY KEY UNIQUE,
                                    name text NOT NULL,
                                    userName text NOT NULL,
                                    PasswordHashed text NOT NULL,
				    UserType text

                                );"""





    createWCNTable = """CREATE TABLE IF NOT EXISTS WCNStoredData (
                                    id integer PRIMARY KEY UNIQUE,
                                    name text NOT NULL,
                                    userName text NOT NULL,
                                    PasswordHashed text NOT NULL,
				    FOREIGN KEY (aliasSystemID) REFERENCES WCNStoredData(id)

                                );"""






    # creates a database connection
    conn = createConnection(databaseFileLocation)


    # creates the following tables if there is a connection
    if conn is not None:

        # creates Sensor feedback table
        createTables(conn, createSensorFeedbackTable)

	# creates Sensor feedin table
        createTables(conn, createSensorFeedinTable)

        # creates Human Machine Interface table
        createTables(conn, createHMITable)

	# creates Wider Company Network table
        createTables(conn, createWCNTable)

        

    else:
        print("The database connection was not established.")


if __name__ == '__main__':
    main()
