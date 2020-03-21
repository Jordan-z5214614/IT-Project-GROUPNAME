let async = require('async'),
parseString = require('xml2js').parseString;
 
let util = require('../Utilities/util'),
devicesDAO = require('../DAO/devicesDAO');
//config = require("../Utilities/config").config;
 

let addDevice = (data, callback) => {
	async.auto({
		device: (cb) => {
			var dataToSet = {
				"ipAddress":data.ipAddress?data.ipAddress:'',
				"host":data.host,
				"deviceid":data.deviceid,
				"projectid":data.projectid
			}
			console.log(dataToSet);
			devicesDAO.addDevice(dataToSet, (err, dbData) => {
			if (err) {
				cb(null, { "statusCode": util.statusCode.FOUR_ZERO_ONE, "statusMessage": util.statusMessage.SERVER_BUSY });
				return;
			}
		
			cb(null, { "statusCode": util.statusCode.OK, "statusMessage": util.statusMessage.DATA_UPDATED,"result":dataToSet });
			});
		}
		//]
	}, (err, response) => {
		callback(response.device);
	});
}
 
let updateDevice = (data,callback) => {
	async.auto({
		deviceUpdate :(cb) =>{
			if (!data.id) {
				cb(null, { "statusCode": util.statusCode.FOUR_ZERO_ONE, "statusMessage": util.statusMessage.PARAMS_MISSING })
				return;
			}
			console.log('phase 1');
			var criteria = {
				id : data.id,
			}
			var dataToSet={
				"ipAddress": data.ipAddress,
				"host":data.host,
				"deviceid": data.deviceid,
				"projectid":data.projectid,
			}
			console.log(criteria,'test',dataToSet);
			devicesDAO.updateDevice(criteria, dataToSet, (err, dbData)=>{
				if(err){
					cb(null,{"statusCode":util.statusCode.FOUR_ZERO_ONE,"statusMessage":util.statusMessage.SERVER_BUSY});
					return; 
				}
				else{
					cb(null, { "statusCode": util.statusCode.OK, "statusMessage": util.statusMessage.DATA_UPDATED,"result":dataToSet });                        
				}
			});
		}
	}, (err,response) => {
		callback(response.deviceUpdate);
	});
}
 
let deleteDevice = (data,callback) => {
	console.log(data,'data to set')
	async.auto({
		removeDevice :(cb) =>{
			if (!data.id) {
				cb(null, { "statusCode": util.statusCode.FOUR_ZERO_ONE, "statusMessage": util.statusMessage.PARAMS_MISSING })
				return;
			}
			var criteria = {
				id : data.id,
			}
			articleDAO.deleteDevice(criteria,(err,dbData) => {
				if (err) {
					console.log(err);
					cb(null, { "statusCode": util.statusCode.FOUR_ZERO_ONE, "statusMessage": util.statusMessage.SERVER_BUSY });
					return;
				}
				cb(null, { "statusCode": util.statusCode.OK, "statusMessage": util.statusMessage.DELETE_DATA });
			});
		}
	}, (err,response) => {
		callback(response.removedevice);
	});
}
 
let getDevices = (data, callback) => {
	async.auto({
		device: (cb) => {
			devicesDAO.getDevices((err, data) => {
				if (err) {
					cb(null, {"errorCode": util.statusCode.INTERNAL_SERVER_ERROR,"statusMessage": util.statusMessage.SERVER_BUSY});
					return;
				}
				cb(null, data);
				return;
			});
		}
	}, (err, response) => {
		callback(response.device);
	})
}
 
let getDeviceDetail = (data, callback) => {
	async.auto({
		device: (cb) => {
			let criteria = {
				"projectid" : data
			}
			devicesDAO.getDeviceDetail(criteria,(err, data) => {
				if (err) {
					console.log(err,'error----');
					cb(null, {"errorCode": util.statusCode.INTERNAL_SERVER_ERROR,"statusMessage": util.statusMessage.SERVER_BUSY});
					return;
				}
				cb(null, data);
				return;
			});
		}
	}, (err, response) => {
		//console.log('in response DAO' + JSON.stringify(response.device));
		callback(response.device);
	})
}
 
module.exports = {
	getDevices : getDevices,
	addDevice : addDevice,
	deleteDevice : deleteDevice,
	updateDevice : updateDevice,
	getDeviceDetail : getDeviceDetail
}
