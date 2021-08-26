#!/bin/bash

# Installation script for OpenLibs package manager

if ((\`id -u\` != 0))
then
  echo 'Please run installer as root or sudo it!'
  exit
fi




pip3 install pyQt5
python3 charging-screen.py
bash requirements-install.sh
python3 openlibs.py
