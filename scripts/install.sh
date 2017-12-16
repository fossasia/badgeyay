#!/usr/bin/env bash
# Install essential packages from Apt
apt-get update -y
# Python dev packages
apt-get install -y build-essential python3 python3-dev python3-setuptools python3-pip
apt-get install -y libssl-dev libffi-dev libjpeg-dev
apt-get install -y libxml2-dev libxslt1-dev
# Install dependencies
apt-get install -y librsvg2-bin pdftk

# Set python3 as default
echo "alias python=python3" >> .bashrc
echo "alias pip=pip3" >> .bashrc

cd /vagrant
#Install requirements
echo "Installing requirements"
pip3 install -r requirements/dev.txt
