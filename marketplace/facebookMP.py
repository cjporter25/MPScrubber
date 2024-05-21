# import os
import sqlite3
import datetime
from bs4 import BeautifulSoup
from datetime import date

from marketplace.constantsFB import *

class facebookMP:
    def __init__(self, minPrice, maxPrice, minMiles, 
                 maxMiles, minYear, maxYear, sorting, 
                 brands, bodyStyles, vehicleTypes):
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.minMiles = minMiles
        self.maxMiles = maxMiles
        self.minYear = minYear
        self.maxYear = maxYear
        self.sorting = sorting
        self.brands = brands
        self.bodyStyles = bodyStyles
        self.vehicleTypes = vehicleTypes
        self.connection = sqlite3.connect('./marketplace/facebookDB.db')
    def __init__(self):
        self.minPrice = "0"
        self.maxPrice = "50000"
        self.minMiles = "0"
        self.maxMiles = "300000"
        self.minYear = "1990"
        self.maxYear = "2024"
        self.sorting = SORTING_FILTERS["Date Listed: Newest First"]
        self.brands = ["Toyota", "Honda", "Chevy"]
        self.bodyStyles = BODYSTYLE_FILTERS["Sedan-SUV-Truck"]
        self.vehicleTypes = VEHICLE_TYPE_FILTERS["Cars & Trucks"]
        self.connection = sqlite3.connect('./marketplace/facebookDB.db')

    def build_URLs(self, brands):
        fbURLs = []
        for brand in brands: 
            url = FB_MP_MAIN + FB_MP_VEHICLES_STPAUL \
                    + PRICE_FILTERS["Min Price"] + self.minPrice \
                    + PRICE_FILTERS["Max Price"] + self.maxPrice \
                    + MILEAGE_FILTERS["Min Mileage"] + self.minMiles \
                    + MILEAGE_FILTERS["Max Mileage"] + self.maxMiles \
                    + YEAR_FILTERS["Min Year"] + self.minYear \
                    + YEAR_FILTERS["Max Year"] + self.maxYear \
                    + self.sorting + MAKE_FILTERS[brand] \
                    + self.bodyStyles + self.vehicleTypes
            urlPlusBrand = [brand, url]
            fbURLs.append(urlPlusBrand)
        return fbURLs
    def validate_db(self):
        cursor = self.connection.cursor()
    def retrieve_postings(self, page_source):
        dbEntries = []
        soup = BeautifulSoup(page_source, features= "html.parser") 
        # Find all postings that are containerized with the following HTML class tag
        postings = soup.body.find_all('div', class_ =  FB_HTML_TAGS["Whole Post"])
        count = 0
        for post in postings:
            if count == 10: #Limit 10 posts at a time
                break
            try:
                link = FB_MAIN + post.find('a', class_ = FB_HTML_TAGS["Link"]).get('href')
            except AttributeError:
                link = "n/a"
            # Find description HTML tag and convert to useable text
            desc = post.find('span', class_ = FB_HTML_TAGS["Description"]).text
            # The vehicle year is currently always the first 4 chars of the description
            year = int(desc[0] + desc[1] + desc[2] + desc[3])
            # Find the price HTML tag and convert to an integer
            price = self.convert_to_int(post.find('span', class_ = FB_HTML_TAGS["Price"]).text)
            # Location and mileage use the same HTML tag for some stupid reason
            locAndMile = post.find_all('span', class_ = FB_HTML_TAGS["Location&Mileage"])
            # The first one is mileage in the format of "55k" or "100k". Remove the letters,
            #   convert to int, and multiply by a 1000 to get the actual number.
            mileage = (self.convert_to_int(locAndMile[1].text)) * 1000
            # The second one is location, simply convert to text
            location = locAndMile[0].text
            
            # Create a primary key for the entry
            primaryKey = self.create_primary_key(year, price, mileage)

            currDateTime = self.get_current_date_and_time()

            # NOTE: Will eventually look work a way to pull the approx time a vehicle was posted
            datePosted = "n/a"

            # Create a new entry tuple. Primary key will always be first item
            newEntry = (primaryKey, currDateTime, datePosted, year, price, mileage, desc, location, link)
            dbEntries.append(newEntry)
            count+=1
        return dbEntries
    
    def create_table(self, brand):
        cursor = self.connection.cursor()
        #deleteCommand = '''DELETE FROM {}'''.format(brand)
        #cursor.execute(deleteCommand)
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
    
    def insert_entries(self, brand, newEntries):
        cursor = self.connection.cursor()
        for entry in newEntries:
            primaryKey = entry[0]
            # Trailing comma indicates the "primaryKey" as a single item tuple
            cursor.execute("SELECT 1 FROM {} WHERE PrimaryKey = ?".format(brand), (primaryKey,))
            existingEntry = cursor.fetchone()

            # If entry already exists, Skip insertion
            if existingEntry:
                print("Entry with primary key '{}' already exists. Skipping insertion.".format(primaryKey))
            else:
                insertCommand = '''INSERT INTO {} VALUES(?,?,?,?,?,?,?,?,?)'''.format(brand)
                cursor.execute(insertCommand, entry)
        #insertManyCommand = '''INSERT INTO {} VALUES(?,?,?,?,?,?,?,?)'''.format(brand)
        #cursor.executemany(insertManyCommand, newEntries)
        self.connection.commit()

    def get_row_count(self, brand):
        cursor = self.connection.cursor()
        query = f"SELECT COUNT(*) FROM {brand}"
        cursor.execute(query)
        rowCount = cursor.fetchone()[0]
        cursor.close()
        return rowCount
    
    def show_table(self, brand):
        cursor = self.connection.cursor()
        select_many_command = '''SELECT * FROM {}'''.format(brand)

        try:
            cursor.execute(select_many_command)
            table = cursor.fetchall()

            # Print table rows excluding the last element. The last element will always be
            #   the URL of the post
            for row in table:
                row_without_url = row[:-1]  # Exclude the last element
                print(row_without_url)
        except sqlite3.Error as e:
            print("Error fetching data:", e)
        finally:
            cursor.close()
    def show_table_ordered(self, brand, order_by_column):
        print("SHOWING TABLE FOR " + brand + " .......")
        cursor = self.connection.cursor()
        select_ordered_command = '''SELECT * FROM {} ORDER BY {}'''.format(brand, order_by_column)

        try:
            cursor.execute(select_ordered_command)
            table = cursor.fetchall()

            # Print table rows
            for row in table:
                row_without_url = row[:-1]  # Exclude the last element
                print(row_without_url)
        except sqlite3.Error as e:
            print("Error fetching data:", e)
        finally:
            cursor.close()

    def list_tables(self):
        cursor = self.connection.cursor()

        # Query sqlite_master table to get a list of all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()

        # Extract table names from the fetched data
        tableList = [table[0] for table in tables]
        
        print("Tables in the database:")
        for tableName in tableList:
            print(tableName)


    def convert_to_int(self, newString):
        try:
            #print("Trying to convert:" + newString)
            numericString = ''.join(c for c in newString if c.isdigit())
            price = int(numericString)
            #print("Converted to:" + numericString)
            return price
        except ValueError as e:
            error_part = newString[e.args[0]:e.args[1]] if isinstance(e.args, tuple) and len(e.args) == 2 else None
            result = {'error': 'ValueError', 'message': str(e), 'entire_string': newString, 'error_part': error_part}
            print("Error occurred during extraction:")
            print("Type:", result['error'])
            print("Message:", result['message'])
            print("Entire string:", result['entire_string'])
            print("Error part:", result['error_part'])
            return 0

    def create_primary_key(self, year, price, mileage):
        unique_id = "{}-{}-{}".format(year, price, mileage)
        return unique_id

    def get_current_date_and_time(self):
        today = date.today()
        currDate = today.strftime("%Y-%m-%d")
        time = datetime.datetime.now().time()
        currTime = time.strftime("%H:%M:%S")
        currDateTime = currDate + "." + currTime
        return currDateTime

# REDACTED
    def save_postings(self, newEntries, brand):
        cursor = self.connection.cursor()
        deleteCommand = '''DELETE FROM ''' + brand
        cursor.execute(deleteCommand)
        newTableCommand = '''CREATE TABLE IF NOT EXISTS ''' + brand + ''' (Year INT, Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)'''
        cursor.execute(newTableCommand)
        addManyCommand = '''INSERT INTO ''' + brand + ''' VALUES(?,?,?,?,?,?)'''
        cursor.executemany(addManyCommand, newEntries)
        self.connection.commit()
        selectMany = '''SELECT * FROM ''' + brand
        cursor.execute(selectMany)
        print(cursor.fetchall())
        self.connection.close()

# REDACTED
    def save_postings_test(self, newEntries, brand):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM Toyota''')
        match brand:
            case "Toyota":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Toyota
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Toyota VALUES(?,?,?,?,?)', newEntries)
            case "Honda":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Honda
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Honda VALUES(?,?,?,?,?)', newEntries)
            case "Chevy":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Chevy
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Chevy VALUES(?,?,?,?,?)', newEntries)
            case "Ford":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Ford
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Ford VALUES(?,?,?,?,?)', newEntries)
            case "Lexus":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Lexus
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Lexus VALUES(?,?,?,?,?)', newEntries)
            case "Dodge":
                cursor.execute('''CREATE TABLE IF NOT EXISTS Dodge
                (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                cursor.executemany('INSERT INTO Dodge VALUES(?,?,?,?,?)', newEntries)
            case _:
                print("Brand provided was not valid, please try again!")
        self.connection.commit()
        test_loc = "Elk River, MN"
        cursor.execute("SELECT * FROM Toyota WHERE Location=?", test_loc)
        print(cursor.fetchall())
        self.connection.close()



                





