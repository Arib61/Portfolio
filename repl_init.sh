#!/bin/bash

# Installer les packages nécessaires pour mysqlclient
sudo apt-get update
sudo apt-get install -y python3-dev default-libmysqlclient-dev build-essential

# Installer les dépendances Python
pip install -r requirements.txt
