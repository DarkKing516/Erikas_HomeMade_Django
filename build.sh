#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update package list and install dependencies
# apt-get update
# apt-get install -y software-properties-common
# apt-get install -y wkhtmltopdf

# Install Python dependencies
pip install -r requirements.txt

# Download and extract portable wkhtmltopdf
curl -L -o wkhtmltopdf.tar.xz https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.bionic_amd64.tar.xz
tar -xf wkhtmltopdf.tar.xz

# Move the binaries to a directory included in PATH
mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

# Clean up
rm -rf wkhtmltopdf.tar.xz wkhtmltox

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
