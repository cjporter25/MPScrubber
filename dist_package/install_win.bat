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

:: List the installed packages
pip list

echo Installation complete. To run the application, a new terminal window will be opened.

:: Open a new terminal window and navigate to the project directory
start powershell -NoExit -Command "cd '%~dp0'; . .venv\Scripts\Activate.ps1; pip list; echo Virtual environment activated. Run 'python main.py' to start the application."

pause