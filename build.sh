#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
# python manage.py migrate

# Setear a db
# python manage.py populate_db

# Start the server 
# gunicorn Erikas_HomeMade.wsgi:application --bind 0.0.0.0:$PORT