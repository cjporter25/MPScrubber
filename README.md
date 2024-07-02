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

## Installation & Usage

1. **Install Python**:
   - RECOMMENDED: Install Python directly from the Microsoft Store.
     This creates the def "Python" PATH. Simply choose the most recent Python version 
     anmdd click "Install".
   - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
   - Make sure to check the box to add Python to your PATH during the installation process.
2. **Install Chrome**:
   - This program currently uses a chrome based web driver to complete it's scrapping functions. If chrome is not installed, this program will not work.

3. **Unzip the Package**:
   - Extract the contents of `mpscrubber_test_build_v_#_#_#.zip` from the test_builds folder
     to some directory. Recommend using the latest version as the remaining instructions are tailored to how it is most recently structured.
   - When choosing a location to extract to, it is recommended that the program be extracted (at this time) to the desktop as the reports will show up there.

3. **Run the Installation Script**:
   - For Windows, double-click the `install_win` file inside the main directory or run it from the command prompt:
     ```bat
     install.bat
     ```
   - NOTE: This is currently not installable on an Apple System!

4. **Run the Application**: PLEASE READ
- Post Install (What to Expect)
   - The installation process will automatically create a python virtual environment that includes all the python modules necessary to make the program work. Once this step is complete, a shortcut labeled "MPScrubber" should appear on the desktop.
- RUN
   - Double click the desktop shortcut and the script will automatically activate the virtual environment and run the program.
- User Prompts (IMPORTANT)
   - The user will be prompted with two options: `Demo` or `Dev-GUI`. The demo has pre-selected scrapping variables to provide the user a demo of what the program currently is capable of. Please do give it time to complete as a chrome window The dev-gui represents the simple GUI that is in development. The eventual goal is to have this GUI be the main driver of user input to scrape the way they want given Facebook's various filtering options.
   - Once the program window is closed, the whole program will exit. To have it run again, simply launch it again through the provided shortcut.
- Demo
   - This demo is preset to scrape for and output the 10 most recently posted used-vehicles from Chevy, Toyota, Ford, Lexus, and Dodge (as of running the program). Unfortuantely, to maintain an up-to-date database, the program would need to run 24/7. Therefore, the output excel sheet will only include the ten most recently added things to the database which could be 10 brand new vehicles at the time of running the script on your own system.


## Folder Structure

### dist
   - When a build is created using the "build" module, via the command "python -m build", 
     the resulting two file types are created - 1. A .tar.gz file which contains the actual 
     source code

### dist-package
   - This contains the .whl and .tar files, the main program files, and the necessary scripts to install and activate a virtual environment, as well as create a shortcut on the desktop for convenience. It holds all the would be folders and files to be a part of a test_build.
   - `dist` - (Not shown) Is still a part of the test_build zip file. Contains the most recent .tar.gz and .whl build.
   - `marketplaceFB` - Contains a direct copy of the files found in the marketplaceFB folder later in this directory
   - `create_shortcut` - An assistive script that runs at the end of the install_win script. Simply creates a shortcut onp the desktop that points to and executes "mpscrubber.ps1" where ever it was extracted to.
   - `install_win` - 
   - `launcher.bat`
   - `main.py` - The main driver of the program. Either outputs the test GUI or runs a pre-set demo of the scrapping and reporting in action
   - `mpscrubber.ps1`
   - `README.md` - An updated README.md to ship with a build

### logs
   - Contains a variety of personal logs to look back on in the event I need to reference a step taken during a past endeavor or conversation. It also includes various text documents simply for my learning to ensure the steps I take are consistently the same each time a build is made.

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
   - `.gitignore` - Created by gitignore.io
   - `LICENSE` - Basic MIT license.
   - `main.py` - Main driver of the program
   - `README.md` - This file
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
