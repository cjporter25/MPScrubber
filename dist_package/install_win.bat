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

:: Install the required packages with verbose output
pip install -r requirements.txt --verbose

:: List the installed packages (No longer necessary)
:: pip list
echo **********************
echo Installation complete. To run the application, a new terminal window will be opened.
echo **********************
echo NOTE: You may be required to allow your computer to run sripts. If so, type in the following
command within any terminal instance and press enter:

echo ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
echo ' Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser '
echo ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

:: Open a new terminal window and navigate to the project directory
start powershell -NoExit -Command "cd '%~dp0'; . .venv\Scripts\Activate.ps1; pip list; echo Virtual environment activated. Type 'python main.py' and press enter to start the application."
echo ****NOTE: Alternative option in the future will include an application run file to avoid the terminal altogether post installation!

pause