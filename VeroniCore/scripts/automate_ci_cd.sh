#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
REPO_URL="https://github.com/your_username/VeroniCore.git"
PROJECT_DIR="/var/www/VeroniCore"
BRANCH="main"
VENV_DIR="$PROJECT_DIR/venv"
BUILD_DIR="$PROJECT_DIR/build"
TEST_RESULTS_DIR="$PROJECT_DIR/test_results"
DEPLOY_LOG="$PROJECT_DIR/deploy.log"

# Start logging
exec &> >(tee -a "$DEPLOY_LOG")

echo "Starting CI/CD automation..."

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

# Run tests
echo "Running tests..."
mkdir -p $TEST_RESULTS_DIR
pytest --junitxml=$TEST_RESULTS_DIR/results.xml

# Build the project (optional step)
echo "Building the project..."
mkdir -p $BUILD_DIR
# Add your build commands here (e.g., npm build, make, etc.)
# Example: python setup.py build

# Deploy the application (e.g., restart services)
echo "Deploying the application..."
sudo systemctl restart gunicorn
sudo systemctl restart nginx

echo "CI/CD automation completed successfully!"
