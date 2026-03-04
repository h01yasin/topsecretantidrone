@echo off
REM ============================================
REM Anti-Drone Defense System - Quick Setup
REM Windows Batch Script
REM ============================================

echo.
echo ========================================
echo  ANTI-DRONE DEFENSE SYSTEM
echo  Quick Setup Script
echo ========================================
echo.

REM Check Python
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.10+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version
echo.

REM Check if venv exists
if exist venv (
    echo [2/6] Virtual environment already exists
) else (
    echo [2/6] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)
echo.

REM Activate venv
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Upgrade pip
echo [4/6] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo.

REM Install requirements
echo [5/6] Installing dependencies...
echo This may take 5-10 minutes...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Try manually: pip install -r requirements.txt
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Download YOLO model
echo [6/6] Downloading YOLOv8 model...
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')" >nul 2>&1
echo Model downloaded!
echo.

REM Success
echo ========================================
echo  SETUP COMPLETE!
echo ========================================
echo.
echo Next steps:
echo   1. Read documentation: README.md
echo   2. Run system: start.bat
echo   3. Or manually: python unified_defense_system.py
echo.
echo Press any key to exit...
pause >nul
