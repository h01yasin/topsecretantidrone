@echo off
REM ============================================
REM Anti-Drone Defense System - Quick Start
REM Windows Batch Script
REM ============================================

echo.
echo ========================================
echo  ANTI-DRONE DEFENSE SYSTEM
echo  Starting...
echo ========================================
echo.

REM Check if venv exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first
    echo.
    pause
    exit /b 1
)

REM Activate venv
call venv\Scripts\activate.bat

REM Check if requirements installed
python -c "import torch" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Dependencies not installed!
    echo Please run setup.bat first
    echo.
    pause
    exit /b 1
)

REM Run the system
echo Starting Anti-Drone Defense System...
echo.
echo Press Ctrl+C to stop
echo.
python unified_defense_system.py

REM If exited
echo.
echo System stopped.
pause
