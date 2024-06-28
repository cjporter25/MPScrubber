# MPSCRUBBER

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation & Usage](#usage)
3. [Folder Structure](#folder-structure)
    - [dist](#dist)
    - [dist_package](#dist_package)
    - [marketplaceCL](#marketplaceCL)
    - [marketplaceFB](#marketplaceFB)
    - [project_images](#project_images)
    - [test_builds](#test_builds)
    - [user_data](#user_data)
    - [Other Files](#other-files)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact](#contact)

## Project Overview
   [Placeholder]

## Potential Use Cases
   [Placeholder]


## Installation & Usage

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
- FOURTH: Choosing "main" or "Dev-GUI"
   - As of right now, choosing "main" will run the program with hard coded presets and 
     "test" will show what the GUI currently looks like.


## Folder Structure

### dist

### dist-package

### logs

### marketplaceCL
   - Currently not in use! If this project expands its scope outside of the facebook marketplace,
   future marketplaces will have dedicated directories for the scripts that run there.

### marketplaceFB
   - `facebookDB.db`
   - `facebookMP_database.py`
   - `facebookMP_GUI.py`
   - `facebookMP_reporting.py`
   - `facebookMP_scraper.py`
   - `facebookMP_variables.py`
   - `GUI_styles.qss`

### project_images
   - Contains a variety of images taken of the project during development. Since this project
   isn't turning into a website, it'll be difficult to necessarily show off what it can do. This
   folder contains images to at least show it off to some degree.

### test_builds
   - Contains the packaged & zipped test builds that are useable and installable by anyone. Will
   hold onto old builds for the sake of continuity and progression comparisons.

### user_data
   - Contains a variety of JSON files that will inevitably be incorporated to elicit a more 
   streamlined and performative user experience, i.e., keeping track of what the apps current
   state was, what was mostly recently queried, etc. This way, redundant scraping won't occur
   and the program will simply spit out what it just did or recently did again.

### Other Files
   - `.gitignore`
   - `LICENSE`
   - `main.py` - Main driver of the program
   - `README.md`
   - `requirements.txt` - Contains the list of python libraries installed in the projects virtual environment
   - `setup.py` - This file contains the necessary structure for the "build" python module to create an installable package
   - `update_setup.py` - Potentially redacted. Was an attempt to automatically update the "install_requires"
     list with the requirements.txt list but it ultimately became too complicated at this time


## Contributing
Contributing and testing is highly encouraged. Web scrapping, at its core is a constantly evolving endeavor as it requires an extreme amount of initial overhead to analyze and understand how
the website you're scrapping is structured. Aside from testing, if the project grows to incorporate
other marketplaces, obtaining the HTML variable data of sed websites would be awesome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or inquiries, please contact "Christopher Porter" at chris.j.porter25@gmail.com
