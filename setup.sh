#!/bin/bash

# Check if running on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Install Homebrew if not installed
    if ! command -v brew &> /dev/null; then
        echo "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Install required system packages
    echo "Installing system dependencies..."
    brew install cmake pkg-config

else
    # For Linux (Ubuntu/Debian)
    echo "Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y cmake pkg-config build-essential
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run the translation script
echo "Running translation script..."
python main.py

# Deactivate virtual environment
deactivate

echo "Done! To reuse the virtual environment later, run: source venv/bin/activate" 