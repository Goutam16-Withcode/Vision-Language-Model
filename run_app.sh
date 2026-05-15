#!/bin/bash
# VLM Bootcamp - Streamlit Frontend Launcher (Linux/Mac)
# This script activates the virtual environment and launches the Streamlit app

echo "======================================"
echo "  VLM Bootcamp Frontend Launcher"
echo "======================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "======================================"
echo "  Launching Streamlit App"
echo "======================================"
echo ""
echo "Opening app at: http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

# Launch Streamlit
streamlit run app.py
