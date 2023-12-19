from bs4 import BeautifulSoup
from options import Options, attrs

#Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Standard Library Imports
import requests 
import os
import logging
import random
import re
import sqlite3
import time
import asyncio
import random
import time

from clmp import *
from fbmp import *

class Selenium():
    def __init__(self):
        os.system("taskkill /f /im chrome.exe")
        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--user-data-dir=C:\\users\\{USER}\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory=Default")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    def get_source(self, url):
        try:
            self.browser.get(url)

            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class='x1gslohp x1e56ztr']")))
            page_source = self.browser.page_source
            return page_source
        except:
            print("Timed Out, or an error occurred while loading")
            return None
    def scrape(self):
        sel = Selenium()
        # URL Schema Order
        prefMinPrice = 0
        prefMaxPrice = 20000
        prefMinMiles = 50000
        prefMaxMiles = 150000
        prefMinYear = 2000
        prefMaxYear = 2015
        prefSorting = "Newest First" # Covered by the statement: SORTING_FILTERS["Date Listed: Newest First"]
        prefMfc = "Toyota" # Facebook only allows one manufacturer selected at a time
        prefBodyStyles = ["Sedan", "SUV", "Truck"] # "&carType=sedan%2Csuv%2Ctruck"
        prefVehicleType = "Cars & Trucks"
        fburl = FB_MP_VEHICLES_STPAUL + PRICE_FILTERS["Min Price"] + str(prefMinPrice) \
                                    + PRICE_FILTERS["Max Price"] + str(prefMaxPrice) \
                                    + MILEAGE_FILTERS["Min Mileage"] + str(prefMinMiles) \
                                    + MILEAGE_FILTERS["Max Mileage"] + str(prefMaxMiles) \
                                    + YEAR_FILTERS["Min Year"] + str(prefMinYear) \
                                    + YEAR_FILTERS["Max Year"] + str(prefMaxYear) \
                                    + SORTING_FILTERS["Date Listed: Newest First"] \
                                    + MAKE_FILTERS["Toyota"] + "&carType=sedan%2Csuv%2Ctruck" \
                                    + VEHICLE_TYPE_FILTERS["Cars & Trucks"]


        page_source = sel.get_source(fburl)
        soup = BeautifulSoup(page_source, 'html.parser')
        postings_list = soup.find_all('div', class_ =  FB_HTML_TAGS["Whole Post"])

        for post in postings_list:
            try:
                description = post.find('span', FB_HTML_TAGS["Description"])
                print(f"Description: {description}")
            except:
                pass
        self.close()
    def close(self):
        self.browser.quit()


sel = Selenium()
sel.scrape()
