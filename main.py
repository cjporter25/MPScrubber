# New System move - 4.15.24 - Christopher J. Porter

#if __name__ == "__main__":
#    app = MainWindow()
#    app.mainloop()

from options import Options, attrs

#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import codecs
import re

# Standard Library Imports
import requests 
import logging
import random
import time
import asyncio
import random
import time
import sys

from craigslistMP import *
from facebookMP import *
from reporting import *


input = input("Running MAIN(1) or TEST(2)? --> ")


rm = ReportsManager()
rm.set_primary_directory()
rm.build_new_report()
    
sys.exit()
#**********************MOCK USER INPUT**********************#
prefMinPrice = 0
prefMaxPrice = 20000
prefMinMiles = 50000
prefMaxMiles = 100000
prefMinYear = 2000
prefMaxYear = 2015
prefSorting = SORTING_FILTERS["Date Listed: Newest First"] # Covered by the statement: SORTING_FILTERS["Date Listed: Newest First"]
prefBrands = ["Chevy", "Honda", "Toyota"] # Facebook only allows one manufacturer selected at a time
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
    #fb.save_postings(newEntries, currBrand)
    print("Mandatory pull delay...")
    time.sleep(3)

driver.quit()



# soup = BeautifulSoup(page_source, features= "html.parser")
# postings = soup.body.find_all('div', class_ =  FB_HTML_TAGS["Whole Post"])
# num_postings = len(postings)
# title = soup.title.text

# file = codecs.open("fb_scraping.txt", 'w') # "w" option means the file will be overwritten
# file.write(title + "\n")
# file.write("These are the postings found on the webpage -->" + "\n")

# count=1

# for post in postings:
#     if count >= 20: #Limit 20 posts at a time
#         break
#     link = post.find('a', class_ = FB_HTML_TAGS["Link"])
#     desc = post.find('span', class_ = FB_HTML_TAGS["Description"])
#     price = post.find('span', class_ = FB_HTML_TAGS["Price"])
#     locAndMile = post.find_all('span', class_ = FB_HTML_TAGS["Location&Mileage"])
#     # print(locAndMile)
#     #mileage = post.find('span', class_ = FB_HTML_TAGS["Mileage"])
#     file.write(str(count) + "." + desc.text + "\n")                 # Desc
#     file.write("  " + price.text + "\n")                            # Price
#     file.write("  " + locAndMile[1].text + "\n")                    # Mileage
#     file.write("  " + locAndMile[0].text + "\n")                    # Location
#     file.write("  " + (FB_MAIN + link.get('href')) + "\n")          # Link
#     count+=1

# file.write("There were " + str(num_postings) + "postings")

# file.close()

#------ REDACTED - NOT NECESSARY TO CLOSE CHROME PRIOR TO RUNNING -----#
#try:
    # Try to kill Chrome process
#    os.system("taskkill /f /im chrome.exe")
#except Exception as e:
    # If an error occurs while killing Chrome process, print the error
#    print("Error occurred while killing Chrome:", e)

#------ NOT COMPLETELY NECESSARY BUT LEAVING FOR PROGRAM VISUAL CLARITY IF NEEDED -----#
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  # Run Chrome in headless mode
#chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (needed in headless mode)
#chrome_options.add_argument("--disable-features=AmbientLightSensor") # Disabling to prevent error
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument(f"--user-data-dir=C:\\users\\{USER}\\AppData\\Local\\Google\\Chrome\\User Data")
#chrome_options.add_argument("profile-directory=Default")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")

