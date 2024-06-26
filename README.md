# MPSCRUBBER

### Installation and Usage Instructions for the Client

1. **Install Python**:
   - RECOMMENDED: Install Python directly from the Microsoft Store.
     This creates the def "Python" PATH. Simply choose the most recent Python version 
     anmdd click "Install".
   - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
   - Make sure to check the box to add Python to your PATH during the installation process.

2. **Unzip the Package**:
   - Extract the contents of `mpscrubber_test_build[v#].zip` from the test_builds folder
     to some directory.
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
- (UPDATED 6.18.24) - The installation script also activates the virtual environment,
  and places the user in a terminal showing the project folder. The user should
  therefore be able to skip to step 3.
- FIRST: Navigate to the project folder
   - cd C:\Users\[USER_ACCOUNT]\Desktop\mpscrubber_test_build\dist_package
- SECOND: Activate the virtual environment
   - .venv\Scripts\Activate.ps1
- THIRD: Run the program
   - python main.py
- FOURTH: Choosing main or "test"
   - As of right now, choosing "main" will run the program with hard coded presets and 
     "test" will show what the GUI currently looks like.

# Summary
   [Placeholder]
# Purpose
   [Placeholder]
# Potential Use Cases
   [Placeholder]
