#!/bin/bash

# Build the project
pip install -r requirements.txt 
python3.9 manage.py collectstatic
