# MPSCRUBBER

## Installation

### Instructions for the Client

1. **Install Python**:
   - RECOMMENDED: Install Python directly from the Microsoft Store.
     This creates the default "Python" PATH.
   - OR - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
   - Make sure to check the box to add Python to your PATH during the installation process.

2. **Unzip the Package**:
   - Extract the contents of `mpscrubber_test_build.zip` to a directory.
   - It is recommended that the program be extracted (at this time) to 
     the desktop as the reports will show up there.

3. **Run the Installation Script**:
   - For Windows, double-click `install.bat` or run it from the command prompt:
     ```bat
     install.bat
     ```
   - For Unix-based systems, run the installation script:
     ```sh
     ./install.sh
     ```

4. **Run the Application**:
- FIRST: Navigate to the project folder
   - cd C:\Users\[USER_ACCOUNT]\Desktop\mpscrubber_test_build\dist_package
- SECOND: Activate the virtual environment
   - venv\Scripts\Activate.ps1
- THIRD: Run the program
   - python main.py