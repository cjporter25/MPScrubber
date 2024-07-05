# import os
import sqlite3
import datetime
import time

from bs4 import BeautifulSoup
from datetime import date

from marketplaceFB.facebookMP_database import *

class FB_Scrapper:
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
        self.connection = sqlite3.connect('./marketplaceFB/facebookDB.db')
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
        self.connection = sqlite3.connect('./marketplaceFB/facebookDB.db')

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
                # www.facebook.com/[link]
                linkTag = post.find('a', class_ = FB_HTML_TAGS["Link"])
                link = linkTag['href']
                fullLink = FB_MAIN + link
            except AttributeError:
                link = "n/a"
            # Find description HTML tag and convert to useable text
            desc = post.find('span', class_ = FB_HTML_TAGS["Description"]).text
            try:
                # The vehicle year is currently always the first 4 chars of the description
                year = int(desc[0] + desc[1] + desc[2] + desc[3])
            except ValueError:
                year = 1900
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

            datePulled = self.get_current_date_and_time()

            # NOTE: Will eventually look work a way to pull the approx time a vehicle was posted
            datePosted = "n/a"

            # Create a new entry tuple. Primary key will always be first item
            newEntry = (primaryKey, datePulled, datePosted, year, price, mileage, desc, location, fullLink)
            dbEntries.append(newEntry)
            count+=1
        return dbEntries

    def convert_to_int(self, newString):
        try:
            # print("Trying to convert:" + newString)
            numericString = ''.join(c for c in newString if c.isdigit())
            price = int(numericString)
            # print("Converted to:" + numericString)
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




                





