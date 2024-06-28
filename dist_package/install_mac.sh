### install_mac.sh

# Create a virtual environment
python3 -m venv .venv

# Check if the virtual environment directory exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not created."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if the virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Error: Virtual environment not activated."
    exit 1
fi

# Install the required packages with verbose output
pip install -r requirements.txt --verbose

echo "**********************"
echo "Installation complete. To run the application, a new terminal window will be opened."
echo "**********************"
echo "NOTE: You may be required to allow your computer to run scripts. If so, you may need to adjust your security settings."

# Open a new terminal window and navigate to the project directory
osascript <<END
tell application "Terminal"
    do script "cd '$(pwd)'; source .venv/bin/activate; pip list; echo Virtual environment activated. Type 'python main.py' and press enter to start the application."
end tell
END

echo "****NOTE: Alternative option in the future will include an application run file to avoid the terminal altogether post installation!"

# Pause (not typically needed in shell scripts, but included here for completeness)
read -p "Press [Enter] key to close this window..."