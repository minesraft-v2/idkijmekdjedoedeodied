#!/bin/bash

echo "=== Bypass Tool Setup ==="

# Check dependencies
command -v python3 >/dev/null 2>&1 || { echo "Python3 required"; exit 1; }
command -v node >/dev/null 2>&1 || echo "Node optional"

# Install Python deps
pip3 install -q requests urllib3 2>/dev/null || echo "Using stdlib only"

# Make scripts executable
chmod +x server.py

echo "Setup complete!"
echo "Run: python3 server.py"
echo "Or open proxy.js and copy to bookmark bar"
