@echo off

:: Create a virtual environment
python -m venv .venv

:: Activate the virtual environment
call .venv\Scripts\Activate.ps1

:: Install the required packages
pip install -r requirements.txt

echo Installation complete. To run the application, a new terminal window will be opened.

:: Open a new terminal window and navigate to the project directory
start powershell -NoExit -Command "cd '%~dp0'; . .venv\Scripts\Activate.ps1; echo Virtual environment activated. Run 'python main.py' to start the application."

pause