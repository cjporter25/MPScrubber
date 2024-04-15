import os
import sqlite3
import datetime
from datetime import date
import openpyxl
from openpyxl import Workbook, load_workbook


class ReportsManager:
    def __init__(self, folderPath):
        self.primaryDir = folderPath
    def __init__(self):
        self.primaryDir = "C:\\Users\\[USER_PROFILE]\\Desktop\\MPScrubberReports"
    
    def set_primary_directory(self):
        user_profile = os.environ.get('USERPROFILE')
        # The following becomes C:\Users\cj_po
        print(user_profile)
        #if user_profile:
        #    print("User profile:", user_profile)
        #else:
        #    print("User profile not found.")

        self.primaryDir = user_profile + "\\Desktop\\MPScrubberReports"
        print(self.primaryDir)


        # Check if the folder exists
        if not os.path.exists(self.primaryDir):
        # Create the folder if it doesn't exist
            os.makedirs(self.primaryDir)
            print("Folder created successfully:", self.primaryDir)
        else:
            print("Folder already exists. No action required.")
    def get_current_date_and_time(self):
        today = date.today()
        currDate = today.strftime("%m-%d-%Y")
        time = datetime.datetime.now().time()
        currTime = time.strftime("%H:%M:%S")
        currDateTime = currDate + "." + currTime
        return currDateTime
    def build_new_report(self):
        currDateTime = self.get_current_date_and_time()
        reportName = "MPReport<" + currDateTime + ">"
        reportFilePath = self.primaryDir + "\\" + reportName
        try:
            # Try to open the Excel file (will raise FileNotFoundError if it doesn't exist)
            with open(reportFilePath):
                pass  # File exists, do nothing
        except FileNotFoundError:
            # File does not exist, create a new Excel file
            workbook = Workbook()
            workbook.save(reportFilePath)
            print("Excel file created successfully:", reportFilePath)