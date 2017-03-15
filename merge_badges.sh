#!/bin/bash

cd "`dirname \"$0\"`"

# https://superuser.com/a/381128
if [ -z "`which rsvg-convert`" ]; then
  sudo apt-get -y install librsvg2-bin
fi
if [ -z "`which python3`" ]; then
  sudo apt-get -y install python3
fi

python3 generate-badges.py


