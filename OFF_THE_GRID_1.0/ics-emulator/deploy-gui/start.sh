#!/bin/bash

rootDir=$PWD

cd "$rootDir/server"

echo ***Starting Server***
cd "$rootDir/server/"
npm start &

echo ***Starting Client***
cd "$rootDir/src/app/"
npm start && fg
