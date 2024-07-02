::install_win.bat

@echo off

:: Create a virtual environment
python -m venv .venv

:: Activate the virtual environment
call .venv\Scripts\activate

:: Check if the virtual environment is activated
if not defined VIRTUAL_ENV (
    echo Error: Virtual environment not activated.
    exit /b 1
)

:: Get ready to install dependencies from build ".whl"
setlocal enabledelayedexpansion
set WHL_FILE=

:: Find any .whl file in the dist folder. There should only be one at this time.
for %%f in ("dist\*.whl") do (
    set WHL_FILE=%%f
)

:: If one is not found, echo there was an error to the console
if "%WHL_FILE%" == "" (
    echo Error: No .whl file found in the dist folder.
    exit /b 1
)

:: If found use "pip install" on the found .whl file with verbose output to 
:: install all requirements for the program
pip install %WHL_FILE% --verbose


echo. 
echo Installation complete. To run the application, double-click the shortcut now on the desktop
echo.
echo NOTE: You may be required to allow your computer to run sripts. If so, type in the 
echo following command within any terminal instance and press enter:
echo.
echo ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
echo ' Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser '
echo ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
echo.


:: Create a shortcut on the desktop.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0create_shortcut.ps1"
pause
