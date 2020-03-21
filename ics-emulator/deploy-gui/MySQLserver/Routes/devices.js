let express = require('express'),
router = express.Router(),
util = require('../Utilities/util'),
deviceService = require('../Services/devices');

router.post('/add-device', (req, res) => {
    console.log("here in add-device");
    deviceService.addDevice(req.body, (data) => {
        res.send(data);
   });
});
 
router.put('/update-device', (req, res) => {
    deviceService.updateDevice(req.body, (data) => {
        res.send(data);
    });
});
 
router.delete('/delete-device', (req, res) => {
    deviceService.deleteDevice(req.query, (data) => {
        res.send(data);
    });
});
 
router.get('/get-devices', (req, res) => {
    deviceService.getDevices(req.query, (data) => {
        res.send(data);
    });
});
 


router.get('/get-device-by-id/:id', (req, res) => {
    deviceService.getDeviceDetail(req.params.id, (data) => {
        res.send(data);
    });
});


var fs = require('fs');
path = require('path');    

router.get('/get-flows/:projectid', (req, res) => {
    filePath = path.join('/home/nol/.nodered/projects/'+req.params.projectid+'/flow.json');
    fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
        if (!err) {
            console.log('received data: ' + data);
            res.send(data);
            //res.send("");
            //response.writeHead(200, {'Content-Type': 'text/html'});
            //response.write(data);
            //response.end();
        } else {
            console.log(err);
            res.send([]);
        }
    });
});
 
module.exports = router;
