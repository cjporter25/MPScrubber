import sqlite3
import time

from marketplaceCG.cargurusMP_variables import *
from mpsTools.util import *

class CG_DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('./marketplaceCG/cargurusDB.db')
        self.numTotalEntries = 0
        self.numExistingEntries = 0
        self.ucBrand = ""
        
    def create_table(self, brand):
        self.ucBrand = brand_name_upper_case(brand)
        print(f"Creating or initializing table for {self.ucBrand}")
        cursor = self.connection.cursor()
        newTableCommand = '''
            CREATE TABLE IF NOT EXISTS {} (
                PrimaryKey TEXT,
                DatePulled TEXT,
                DatePosted TEXT,
                Year INT,
                Price INT,
                Mileage INT,
                Description TEXT,
                Location TEXT,
                Link TEXT
            )'''.format(brand)
        cursor.execute(newTableCommand)
        self.connection.commit()
