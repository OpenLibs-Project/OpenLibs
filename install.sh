#!/bin/bash

# Installation script for OpenLibs package manager

if ((\`id -u\` != 0))
then
  echo 'Please run installer as root or sudo it ~ root privileges needed'
  exit
fi

cd ..
cp OpenLibs OpenLibs-v1.0
rm -rf /usr/local/bin/OpenLibs-v1.0/
rm -r /usr/local/bin/OpenLibs-v1.0/
mv OpenLibs-v1.0 /usr/local/bin/
cd /usr/local/bin/Open:ibs-v1.0/

#python3 charging-screen.py
#pip3 install pyQt5

cd ..
touch openlibs-cli
echo "python3 /usr/local/bin/OpenLibs-v1.0/openlibs.py" >> openlibs-cli
chmod +x openlibs-cli
echo "To run OpenLibs Interactive CLI use <openlibs-cli> command"
