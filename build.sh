#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create a directory for wkhtmltopdf in the home directory
mkdir -p $HOME/bin

# Download and extract portable wkhtmltopdf
curl -L -o wkhtmltopdf.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
dpkg -x wkhtmltopdf.deb wkhtmltopdf

# Move the binaries to a directory included in PATH
cp wkhtmltopdf/usr/local/bin/wkhtmltopdf $HOME/bin/wkhtmltopdf

# Ensure the binaries are executable
chmod +x $HOME/bin/wkhtmltopdf

# Clean up
rm -rf wkhtmltopdf.deb wkhtmltopdf

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
# python manage.py migrate

# Setear a db
python.exe .\manage.py populate_db
# Start the server 
# gunicorn Erikas_HomeMade.wsgi:application --bind 0.0.0.0:$PORT
./paraquenosecierre.sh &
