#!/bin/bash

rootDir=$PWD

cd "$rootDir/server"

echo ***Setting Up Client***
cd "$rootDir/src/app/"
npm i

echo ***Setting Up Server***
cd "$rootDir/server/"
npm i
#additional npm installs
npm install node-red-contrib-modbus
npm install node-red-dashboard
npm install node-red-node-pi-neopixel
npm install node-red-contrib-aggregator
npm install mysql

echo ***Starting Server***
npm start &

echo ***Starting Client***
cd "$rootDir/src/app/"
npm start && fg
