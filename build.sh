#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update package list and install dependencies
# apt-get update
# apt-get install -y software-properties-common
# apt-get install -y wkhtmltopdf

# Install Python dependencies
pip install -r requirements.txt

# Download and install wkhtmltopdf
curl -L -o wkhtmltopdf.tar.xz https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.tar.xz
mkdir -p /tmp/wkhtmltopdf
tar -xvf wkhtmltopdf.tar.xz -C /tmp/wkhtmltopdf --strip-components=1
mv /tmp/wkhtmltopdf/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
