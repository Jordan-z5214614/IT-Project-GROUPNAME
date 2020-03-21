/*
Node-Red node to utilise the arduino motor hat on a raspberry pi.
Levereages the excellent work of J. Cane on the motor-hat project
https://github.com/jcane86/motor-hat
*/
let spec = {
    address: 0x60,
    dcs: ['M1', 'M2'],
};

var motorHat = require('motor-hat')(spec);

motorHat.init();

// HARD CODED FOR TESTING ONLY
// Test DC motor M1
// Set speed to 50%
motorHat.dcs[0].setSpeed(50);
// Start M1 in 'FWD' direction
motorHat.dcs[0].run('fwd');

// Test DC motor M2
// Set speed to 50%
motorHat.dcs[1].setSpeed(50);
// Start M2 in REV direction
motorHat.dcs[1].run('back');

// stop the dc motors
motorHat.dcs[0].stop((err) => !err && console.log("M1 Stopped"));
motorHat.dcs[1].stop((err) => !err && console.log("M2 Stopped"));


