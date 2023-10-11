#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear