@echo off
echo Cursor ID Manager - Windows Runner
echo ============================

:: Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Run the script
python cursor_id_manager.py %*
pause 