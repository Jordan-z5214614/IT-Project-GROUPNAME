# QuickStart

Prepare SD with Raspbian, ensuring you add in the `config.txt` file and `SSH` file to the root directory of the SD image to allow SSH, I2C and SPI protocols.

Plug in pi to router and power on, allow some time for pi to boot. Find the Raspberry Pi network location via a DHCP table or other means.

ssh into the pi using the standard credentials `u:pi p:raspberry`

Once connected run the following
```
sudo apt get update -y 
sudo apt upgrade -y
```
This may take a while depending on how current the SD image was. Then run:
```
sudo apt install git -y
git clone https://github.com/Mikaela199/OFF-THE-GRID.git
cd ./OFF-THE-GRID/ics-emulator/deploy-raspberry-pi
sudo /bin/bash deploy_offTheGrid.sh
```
Then follow the prompts, the script will eventually reboot the raspberry pi, logging you out of your session. Wait a short time then log back in and resume setup.

The next step creates the custom image for your client and server configured Raspberry Pis. Run:
```
sudo /bin/bash docker-make.sh
```
This can take a while depending on the system. Once complete, to start your node-red instance on docker run:

```
docker run -it -p1880:1880 -p502:502 testing:node-red-build
```
Note: To run the motor hat and neopixels you will need to give the docker image access to these devices in the run command:
```
docker run -it -p1880:1880 -p502:502 --device /dev/i2c-0 --device /dev/i2c-1 testing:node-red-build
```
## Note
If using modbus open the port from docker to the pi using the ```-p 502:502``` command, this may require sudo priveledge to run on the host machine as this port (502) is a priveledged port.
