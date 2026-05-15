@echo off
REM VLM Bootcamp - Streamlit Frontend Launcher (Windows)
REM This script activates the virtual environment and launches the Streamlit app

echo ======================================
echo   VLM Bootcamp Frontend Launcher
echo ======================================
echo.

REM Check if venv exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install/update dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ======================================
echo   Launching Streamlit App
echo ======================================
echo.
echo Opening app at: http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

REM Launch Streamlit
streamlit run app.py

pause
