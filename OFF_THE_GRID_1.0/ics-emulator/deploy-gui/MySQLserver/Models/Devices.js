let mysqlConfig = require("../Utilities/mysqlConfig");
 
let initialize = () => {
mysqlConfig.getDB().query("create table IF NOT EXISTS devicetable (id INT auto_increment primary key, ipAddress VARCHAR(30), host VARCHAR(30),deviceid VARCHAR(24),projectid VARCHAR(24) DEFAULT NULL)");
 
}
 
module.exports = {
initialize: initialize
}