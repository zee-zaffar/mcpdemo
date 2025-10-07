#!/bin/bash
# Post-build script for Azure App Service deployment

echo "Starting post-build script..."

# Install Python dependencies
echo "Installing Python dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Post-build script completed successfully!"