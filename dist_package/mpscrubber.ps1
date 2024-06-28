# mpscrubber.ps1

# Activate the virtual environment
. "$PSScriptRoot\.venv\Scripts\Activate.ps1"

# Run the application using pythonw.exe
Start-Process "$PSScriptRoot\.venv\Scripts\pythonw.exe" -ArgumentList "main.py"