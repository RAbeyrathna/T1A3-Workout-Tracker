#!/bin/bash

if python3 --version &>/dev/null; then
    python3 -m venv .venv
    source .venv/bin/activate

    pip3 install -r ./requirements.txt

    python3 main.py
else
    echo "Error: Python was not detected. This application used Python to run. Please install Python 3 before running this application"
    exit 1
fi