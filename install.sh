#!/bin/bash

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y i2c-tools
sudo pip3 install mysql-connector-python
sudo apt install python3-pip
sudo pip3 install sht20
sudo pip3 install smbus2
