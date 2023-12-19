#!/bin/bash

if python3 --version &>/dev/null; then
    python3 -m venv .venv
    source .venv/bin/activate

    pip3 install colored
    pip3 install prettytable

    python3 main.py
else
    echo "Python was not detected. Please install Python before running this application"
fi