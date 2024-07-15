# import os
import sqlite3
import time

from marketplaceFB.facebookMP_variables import *


class FB_DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('./marketplaceFB/facebookDB.db')
        self.numTotalEntries = 0
        self.numExistingEntries = 0
        self.ucBrand = ""
        
        
    def create_table(self, brand):
        self.set_brand_name_upper_case(brand)
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
    
    def insert_entries(self, brand, newEntries):
        print(f"Inserting new entries for {self.ucBrand}")
        cursor = self.connection.cursor()
        insertionsSkipped = 0
        for entry in newEntries:
            primaryKey = entry[0]
            # Trailing comma indicates the "primaryKey" as a single item tuple
            cursor.execute("SELECT 1 FROM {} WHERE PrimaryKey = ?".format(brand), (primaryKey,))
            existingEntry = cursor.fetchone()

            # If entry already exists, Skip insertion
            if existingEntry:
                insertionsSkipped = insertionsSkipped + 1
            else:
                insertCommand = '''INSERT INTO {} VALUES(?,?,?,?,?,?,?,?,?)'''.format(brand)
                cursor.execute(insertCommand, entry)
        self.set_num_existing_entries(insertionsSkipped)
        self.connection.commit()

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
    def show_brand_meta_data(self, brand):
        print(f"Current total for {self.ucBrand}: {str(self.fetch_total_number_of_entries(brand))}")
        print(f"Number of entries already present for {self.ucBrand}: {str(self.get_num_existing_entries())}")


    def fetch_brand_list(self):
        cursor = self.connection.cursor()
        # Query sqlite_master table to get a list of all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        # Extract table names from the fetched data
        tableList = [table[0] for table in tables]

        # Close the cursor and connection
        cursor.close()
        return tableList
    def fetch_total_number_of_entries(self, brand):
        cursor = self.connection.cursor()
        query = f"SELECT COUNT(*) FROM {brand}"
        cursor.execute(query)
        rowCount = cursor.fetchone()[0]
        cursor.close()
        self.set_num_total_entries(rowCount)
        return rowCount
    def fetch_mileage_and_prices_most_recent(self, brand):
        cursor = self.connection.cursor()
        sortingType = "DatePulled"
        query = f'SELECT PrimaryKey, Mileage, Price FROM {brand} ORDER BY {sortingType} DESC'
        # Fetch data sorted by DatePulled in descending order for the specified brand
        cursor.execute(query)
        # Fetch "numPostings" worth of most recent entries
        data = cursor.fetchmany(15)
        return data
    def fetch_mileage_and_prices_all(self, brand):
        cursor = self.connection.cursor()
        query = f'SELECT Mileage, Price FROM {brand}'
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    def fetch_details_by_primary_key(self, brand, primaryKey):
        cursor = self.connection.cursor()
        query = f'SELECT PrimaryKey, Year, Price, Mileage, Description, Location, Link FROM {brand} WHERE PrimaryKey = ?'
        cursor.execute(query, (primaryKey,))
        row = cursor.fetchone()
        if row:
            return {row[0]: {"year": row[1], "price": row[2], "mileage": row[3], "description": row[4], "location": row[5], "link": row[6]}}
        return {}

    def get_num_total_entries(self):
        return self.numTotalEntries
    def get_num_existing_entries(self):
        return self.numExistingEntries
    def set_num_existing_entries(self, existingEntries):
        self.numExistingEntries = existingEntries
    def set_num_total_entries(self, totalEntries):
        self.numTotalEntries = totalEntries
    def set_brand_name_upper_case(self, brand):
        self.ucBrand = brand.upper()
    def wait(self):
        print("Automated Detection System Prevention. Waiting 5 seconds before scrapping the next brand...")
        for i in range(5, 0, -1):
            print("...")
            time.sleep(1)