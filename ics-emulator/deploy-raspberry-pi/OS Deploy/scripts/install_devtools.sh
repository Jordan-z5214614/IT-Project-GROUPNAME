#!/bin/bash
set -ex

# Installing Devtools
if [[ ${TAG_SUFFIX} != "minimal" ]]; then
  echo "Installing devtools"
  apk add --no-cache --virtual devtools build-base linux-headers udev python python3 python3-dev
  pip3 install --upgrade pip
  pip3 install --upgrade setuptools
  pip3 install rpi_ws281x adafruit-circuitpython-neopixel
  pip3 install adafruit-circuitpython-motorkit  
else
  echo "Skip installing devtools"
fi
