#!/bin/bash

# Add command to check if Python is installed - Print error message to user to install python 

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install prettytable
python3 main.py