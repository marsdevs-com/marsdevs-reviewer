#!/bin/bash
# Script to build and publish MarsDevs Reviewer to PyPI

set -e

echo "Building MarsDevs Reviewer package..."

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build the package
python3 -m pip install --upgrade build twine
python3 -m build

echo ""
echo "Build complete! Files created:"
ls -la dist/

echo ""
echo "To upload to TEST PyPI (recommended first):"
echo "  python3 -m twine upload --repository testpypi dist/*"
echo ""
echo "To upload to PyPI:"
echo "  python3 -m twine upload dist/*"
echo ""
echo "Make sure you have configured your PyPI credentials in ~/.pypirc"