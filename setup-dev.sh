#!/bin/bash
# Quick development setup script

echo "Setting up MarsDevs Code Reviewer development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install package in development mode
echo "Installing package in development mode..."
pip install -e .

# Install development dependencies
echo "Installing development dependencies..."
pip install -r requirements-dev.txt

echo ""
echo "✅ Development environment ready!"
echo ""
echo "To activate the environment in the future:"
echo "  source venv/bin/activate"
echo ""
echo "To test the CLI:"
echo "  marsdevs-reviewer --help"
echo ""
echo "To deactivate:"
echo "  deactivate"