#!/bin/bash
 
# Since: 02/09/19
# Author: ryan.walsh@student.unsw.edu.au
# Version: 1.0
# Description: 
# Team OFF THE GRID raspberry pi init script to automate a fresh
# Raspberry Pi deployment

#TODO: 
# - Offer alternative username creation and delete default pi user
# - Fix hostname change to resolve conflicts in subnet

# Welcome

# Root User Check
if [ "$EUID" != "0" ]
  then
  echo -e "\n#########################################################################" 
  echo -e "\t Root user not detected"
  echo -e "#########################################################################"
  read -p "Must be root to carry out script. Continue anyway? (y/N) ? " yn
  case $yn in
    [Yy]* )
    ;;
    * )
      exit
    ;;
  esac
fi
echo -e "\n#########################################################################"
  echo -e "\t Change Default Passwords!"
echo -e "\n#########################################################################\n"
read -s -e -p "Enter new pass for pi: " pass1
echo "pi:$pass1" | chpasswd
echo -e "\n#########################################################################\n"
read -s -e -p "Enter new pass for root: " pass2
echo "root:$pass2" | chpasswd

echo -e "\n#########################################################################"
echo -e "\t Updating apt cache and upgrading..."
echo -e "#########################################################################"
# Update cache
sudo apt get update -y 
sudo apt upgrade -y

echo -e "\n#########################################################################"
echo -e "\t Installing Docker..."
echo -e "#########################################################################"
# Install docker
read -p "Install Docker now? (y/N) ? " yn
case $yn in
  [Yy]* )
  sudo curl -sSL https://get.docker.com | sh
  ;;
  * )
  ;;
esac


# Add current user as admin for Docker
echo -e "\n#########################################################################"
echo -e "\t Adding Docker user rights"
echo -e "#########################################################################"
sudo usermod -a -G docker $USER
sudo usermod -a -G docker pi
sudo systemctl enable docker

# Add persistence for a data folder for docker to save itesm outside container
echo -e "\n#########################################################################"
echo -e "\t Adding a local docker user directory"
echo -e "#########################################################################"
mkdir -p /home/pi/node-red/data
sudo chown -R 1000:1000 /home/pi/node-red/data
sudo chmod 755 /home/pi/node-red/data

echo -e "\n#########################################################################"
echo -e "\t Installing Local Node-Red as sudo..."
echo -e "#########################################################################"
sudo apt install build-essential -y
wget https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered
sudo /bin/bash update-nodejs-and-nodered
#sudo bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

echo -e "\n#########################################################################"
echo -e "\t Installing Python Libraries..."
echo -e "#########################################################################"
sudo apt install python3 python3-pip -y
sudo pip3 install --upgrade setuptools 
pip3 install RPI.GPIO
pip3 install adafruit-blinka
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
pip3 install adafruit-circuitpython-motorkit


# Add a nice Off The Grid login screen for client
echo -e "\n#########################################################################"
echo -e "\t CAUTION! The following choices must only be run once!"
echo -e "#########################################################################"
read -p "Add a useful SSH login RPi status banner? (y/N) ? " yn
case $yn in
  [Yy]* )
	echo "Adding banner to $user file"
	sudo cat ./banner.txt >> /home/pi/.bashrc
  ;;
  * )
  ;;
esac

# disable sound card to allow less noisy GPIO for LED
echo -e "\n#########################################################################"
echo -e "\t Disabling the sound card for better/less noisy clock rate"
echo -e "#########################################################################"
echo 'blacklist snd_bcm2835' | sudo tee /etc/modprobe.d/raspi-blacklist.conf > /dev/null 2>&1


# Change Hostnames - clean up network names for scenario
echo -e "\n#########################################################################"
echo -e "\t Change hostname to clean up subnet naming"
echo -e "#########################################################################"
OLD_HOSTNAME="$( hostname )"
NEW_HOSTNAME="$1"

if [ -z "$NEW_HOSTNAME" ]; then
 echo -n "Please enter new hostname: "
 read NEW_HOSTNAME < /dev/tty
fi

if [ -z "$NEW_HOSTNAME" ]; then
 echo "Error: no hostname entered. Exiting..."
 exit 1
fi

echo "Changing hostname from $OLD_HOSTNAME to $NEW_HOSTNAME..."

hostname "$NEW_HOSTNAME"

sed -i "s/HOSTNAME=.*/HOSTNAME=$NEW_HOSTNAME/g" /etc/hostname

if [ -n "$( grep "$OLD_HOSTNAME" /etc/hosts )" ]; then
 sed -i "s/$OLD_HOSTNAME/$NEW_HOSTNAME/g" /etc/hosts
else
 echo -e "$( hostname -I | awk '{ print $1 }' )\t$NEW_HOSTNAME" >> /etc/hosts
 sleep 1
 echo '$NEW_HOSTNAME' | sudo tee /etc/hostname > /dev/null 2>&1
fi

echo "Hostname changed."


echo -e "\n#########################################################################"
echo -e " Please enable I2C and SPI interfaces in the following page..."
echo -e "#########################################################################"

sleep 5

sudo raspi-config

echo -e "\n#########################################################################"
echo -e "\t\tSYSTEM REQUIRES REBOOT TO SET CHANGES."
echo -e "#########################################################################"

read -p "Reboot now?[Recommended] (y/N) ? " yn
case $yn in
  [Yy]* )
	echo "Rebooting...."
	sleep 2
	sudo reboot
  ;;
  * )
  ;;
esac