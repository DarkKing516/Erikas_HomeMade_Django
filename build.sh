#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update package list and install dependencies
# apt-get update
# apt-get install -y software-properties-common
# apt-get install -y wkhtmltopdf

# Install Python dependencies
pip install -r requirements.txt

# Create a directory for wkhtmltopdf in the home directory
mkdir -p $HOME/bin

# Download and extract portable wkhtmltopdf
curl -L -o wkhtmltopdf.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
dpkg -x wkhtmltopdf.deb wkhtmltopdf

# Move the binaries to a directory included in PATH
cp wkhtmltopdf/usr/local/bin/wkhtmltopdf $HOME/bin/wkhtmltopdf

# Clean up
rm -rf wkhtmltopdf.deb wkhtmltopdf

# Update package list and install dependencies
apt-get update
apt-get install -y software-properties-common
apt-get install -y wkhtmltopdf

# Check if wkhtmltopdf is installed and accessible
if ! command -v wkhtmltopdf &> /dev/null
then
    echo "wkhtmltopdf could not be found"
    exit
fi

# Print the path to wkhtmltopdf
which wkhtmltopdf

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
