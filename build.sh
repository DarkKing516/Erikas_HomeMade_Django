#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create a directory for wkhtmltopdf in the home directory
mkdir -p $HOME/bin

# Download and extract portable wkhtmltopdf
curl -L -o wkhtmltopdf.tar.gz https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.focal_amd64.tar.gz
tar -xvzf wkhtmltopdf.tar.gz -C $HOME/bin --strip-components=2 wkhtmltox/bin/wkhtmltopdf

# Ensure the binaries are executable
chmod +x $HOME/bin/wkhtmltopdf

# Clean up
rm wkhtmltopdf.tar.gz

# Export the path
export PATH=$HOME/bin:$PATH

# Verify installation
if ! command -v wkhtmltopdf &> /dev/null
then
    echo "wkhtmltopdf could not be found"
    exit 1
fi

# Print the path to wkhtmltopdf
which wkhtmltopdf

# Collect static files
python manage.py collectstatic --no-input || true

# Apply any outstanding database migrations
python manage.py migrate

# Start the server
gunicorn erikas_homemade.wsgi:application --bind 0.0.0.0:$PORT
