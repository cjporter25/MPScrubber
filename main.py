# New System move - 4.15.24 - Christopher J. Porter

# from options import Options, attrs ////

#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
#import codecs ////
#import re ////

# Standard Library Imports
# import requests //// 
# import logging ////
# import random ////
import time
# import asyncio ////
# import random ////
import time
# import sys ////

from craigslistMP import *
from facebookMP import *
from reporting import *


input = input("Running MAIN(1) or TEST(2)? --> ")
    
#sys.exit()
#**********************MOCK USER INPUT**********************#
prefMinPrice = 0
prefMaxPrice = 20000
prefMinMiles = 50000
prefMaxMiles = 100000
prefMinYear = 2000
prefMaxYear = 2015
prefSorting = SORTING_FILTERS["Date Listed: Newest First"] # Covered by the statement: SORTING_FILTERS["Date Listed: Newest First"]
#prefBrands = ["Chevy", "Honda", "Toyota", "Ford", "Lexus", "Dodge"] # Facebook only allows one manufacturer selected at a time
prefBrands = ["Chevy", "Honda", "Lexus"]
prefBodyStyles = BODYSTYLE_FILTERS["Sedan-SUV-Truck"] # "&carType=sedan%2Csuv%2Ctruck"
prefVehicleType = VEHICLE_TYPE_FILTERS["Cars & Trucks"]
#**********************MOCK USER INPUT**********************#

fb = facebookMP()
urls = fb.build_URLs(prefBrands)
newDate = fb.get_current_date_and_time()
print(newDate)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)

#EXAMPLE
# for item in myList:
#    brand = item[0]
#    url = item[1]
#    print(f"Brand: {brand}, URL: {url}")

for url in urls:
    try:
        # url[1] contains the actual built URL
        driver.get(url[1]) #Get the URL's data
        get_url = driver.current_url #Retrieve what the driver used as the URL
        wait.until(EC.url_to_be(url[1])) #Wait to let the page load
        if get_url == url[1]:    #If the used URL matches the original, grab the page source
            page_source = driver.page_source
    except:
        print("Timed Out, or an error occurred while loading")

    # url[0] contains a string of the current brand
    currBrand = url[0]

    print("Retrieving posting data...")
    newEntries = fb.retrieve_postings(page_source)
    time.sleep(1)
    print("Creating or initializing table for " + currBrand + "...")
    fb.create_table(currBrand)
    time.sleep(1)
    print("Inserting new entries...")
    fb.insert_entries(currBrand, newEntries)
    time.sleep(1)
    fb.show_table_ordered(currBrand, "PrimaryKey")
    print(fb.get_row_count(currBrand))
    print("Mandatory pull delay...")
    fb.list_tables()
    time.sleep(3)

driver.quit()

rm = ReportsManager()
rm.set_primary_directory()
rm.build_new_report()