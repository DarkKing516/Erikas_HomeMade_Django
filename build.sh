#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update package list and install dependencies
# apt-get update
# apt-get install -y software-properties-common
# apt-get install -y wkhtmltopdf

# Install Python dependencies
pip install -r requirements.txt

# # Update package list and install dependencies
# apt-get update
# apt-get install -y software-properties-common
# apt-get install -y wkhtmltopdf

# # Check if wkhtmltopdf is installed and accessible
# if ! command -v wkhtmltopdf &> /dev/null
# then
#     echo "wkhtmltopdf could not be found"
#     exit
# fi

# Print the path to wkhtmltopdf
# which wkhtmltopdf

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
