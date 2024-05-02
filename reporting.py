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
        # user_profile becomes C:\Users\cj_po
        print(user_profile)
        self.primaryDir = user_profile + "\\Desktop\\MPScrubberReports"
        print(self.primaryDir)

        # Check if the folder exists
        if not os.path.exists(self.primaryDir):
        # Create the folder if it doesn't exist
            os.makedirs(self.primaryDir)
            print("Folder created successfully:", self.primaryDir)
        else:
            print("Folder already exists. No action required.")
    def build_new_report(self):
        currDateTime = self.get_current_date_and_time()
        # Excel file type = .xlsx
        reportFileName = "MPReport(" + currDateTime + ").xlsx"
        reportFilePath = self.primaryDir + "\\" + reportFileName

        if not os.path.exists(reportFilePath):
            workbook = Workbook()
            print(reportFilePath)
            workbook.save(reportFilePath)
            print("Excel file created successfully:", reportFilePath)
        else:
            pass
        

    def get_current_date_and_time(self):
        today = date.today()
        currDate = today.strftime("%m-%d-%Y")
        time = datetime.datetime.now().time()
        currTime = time.strftime("%H.%M.%S")
        currDateTime = currDate + "-" + currTime
        return currDateTime