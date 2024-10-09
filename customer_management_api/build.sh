#!/usr/bin/env bash
# Exit on error
set -o errexit
pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations customers

python manage.py migrate