import os
import sqlite3
import json

import datetime
from datetime import date
import openpyxl
from openpyxl import Workbook, load_workbook


class ReportsManager:
    def __init__(self, folderPath):
        self.primaryDir = folderPath
        self.conn = sqlite3.connect('./marketplace/facebookDB.db')
    def __init__(self):
        self.primaryDir = "C:\\Users\\[USER_PROFILE]\\Desktop\\MPScrubberReports"
        self.conn = sqlite3.connect('./marketplace/facebookDB.db')
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
        brandList = self.get_brand_list(self)
        print("List of brands (tables) in the database:")
        print(brandList)
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
    def get_brand_list(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        brands = [table[0] for table in tables]
        return brands
    def get_current_date_and_time(self):
        today = date.today()
        currDate = today.strftime("%Y-%m-%d")
        time = datetime.datetime.now().time()
        currTime = time.strftime("%H.%M.%S")
        currDateTime = currDate + "-" + currTime
        return currDateTime