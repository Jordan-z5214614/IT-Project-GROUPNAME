Go to the deploy-gui/MySQLserver/ directory and perform the following steps

1. update the Utilities/config.js file with database username,password and name.
2. create the database in your mysql server. 
3. Run the following query to generate table in database => create table IF NOT EXISTS devicetable (id INT auto_increment primary key, ipAddress VARCHAR(30), host VARCHAR(30),deviceid VARCHAR(24),projectid VARCHAR(24) DEFAULT NULL)
4. run ```npm i``` to install all the necessary packages
5. run ```nodemon server.js``` to serve API server instance

