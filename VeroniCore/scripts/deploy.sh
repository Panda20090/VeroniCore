#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Define variables
REPO_URL="https://github.com/your_username/VeroniCore.git"
PROJECT_DIR="/var/www/VeroniCore"
VENV_DIR="$PROJECT_DIR/venv"
BRANCH="main"

echo "Starting deployment of VeroniCore..."

# Pull the latest code from the repository
if [ -d "$PROJECT_DIR" ]; then
    echo "Pulling the latest code..."
    cd $PROJECT_DIR
    git pull origin $BRANCH
else
    echo "Cloning the repository..."
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
    git checkout $BRANCH
fi

# Check if virtual environment exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files (for Django applications)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Restart application (for Gunicorn and Nginx setup)
echo "Restarting application..."
sudo systemctl restart gunicorn
sudo systemctl restart nginx

echo "Deployment completed successfully!"
