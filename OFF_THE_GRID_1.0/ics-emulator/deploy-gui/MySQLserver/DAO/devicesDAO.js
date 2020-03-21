let dbConfig = require("../Utilities/mysqlConfig");
let getDevices = (callback) => {
    //criteria.aricle_id ? conditions += ` and aricle_id = '${criteria.aricle_id}'` : true;
    dbConfig.getDB().query(`select * from devicetable where 1`,callback);
}
 
let getDeviceDetail = (criteria, callback) => {
    dbConfig.getDB().query('select * from devicetable where projectid = \"'+criteria.projectid+'\"' , callback);
}
 
let addDevice = (dataToSet, callback) => {
    console.log("insert into deviceTable set ? ", dataToSet);
    dbConfig.getDB().query("insert into devicetable set ? ", dataToSet, callback);
}
 
let deleteDevice = (criteria, callback) => {
    let conditions = "";
    criteria.id ? conditions += ` and id = '${criteria.id}'` : true;
    console.log(`delete from deviceTable where 1 ${conditions}`);
    dbConfig.getDB().query(`delete from devicetable where 1 ${conditions}`, callback);
 
}
 
let updateDevice = (criteria,dataToSet,callback) => {
    let conditions = "";
    let setData = "";
    criteria.id ? conditions += ` and id = '${criteria.id}'` : true;
    dataToSet.category ? setData += `category = '${dataToSet.category}'` : true;
    dataToSet.title ? setData += `, title = '${dataToSet.title}'` : true;
    console.log(`UPDATE deviceTable SET ${setData} where 1 ${conditions}`);
    dbConfig.getDB().query(`UPDATE devicetable SET ${setData} where 1 ${conditions}`, callback);
}
module.exports = {
    getDevices : getDevices,
    addDevice : addDevice,
    deleteDevice : deleteDevice,
    updateDevice : updateDevice,
    getDeviceDetail : getDeviceDetail
}
