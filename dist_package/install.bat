@echo off

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install the required packages
pip install -r requirements.txt

echo Installation complete. To run the application, activate the virtual environment and run 'python main.py'.
pause