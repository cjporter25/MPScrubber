# import os
import sqlite3
import datetime
import time
import os
import requests
import pprint

from bs4 import BeautifulSoup
from datetime import date
import urllib.parse

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


from marketplaceCG.cargurusMP_database import *
from mpsTools.util import *


class CG_Scrapper:
    def __init__(self, startYear="2000", endYear="2024", minPrice="0", 
                 maxPrice="50000", maxMileage="200000", brands=None,
                 zipcode=None, distance="50", sorting=None):
        self.startYear = startYear
        self.endYear = endYear
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.maxMileage = maxMileage
        self.brands = brands if brands is not None else DEF_BRAND_ONE
        self.zipcode = zipcode if zipcode is not None else DEF_ZIP
        self.distance = distance
        self.sorting = sorting if sorting is not None else CG_SORTING_FILTERS["Best deals first"]
    def scrape(self):
        newDate = get_formatted_date_and_time()
        print(f"Current date and time: {newDate}")
        cgURLs = self.cg_build_URLs(self.brands)
        driver = self.cg_build_custom_driver()
        '''
        headers = CUSTOM_HEADERS
        decoded_cookie = urllib.parse.unquote(CG_COOKIE)
        headers['Cookie'] = decoded_cookie
        for url in cgURLs:
            referer = url[2]
            headers['Referer'] = referer
            pprint.pprint(headers)
            response = requests.get(url[1], headers=headers)
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                # Your parsing logic here
                print(soup.prettify())
            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        '''

        # Open each URL 
        for url in cgURLs:
            try:
                # url[1] contains the actual built URL
                driver.get("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=m24&zip=55401") #Get the URL's data
                time.sleep(10)
                page_source = driver.page_source
            except Exception as e:
                print(f"Error occurred while loading URL {url[1]}: {e}")
                continue

            # url[0] contains a string of the current brand being looked at
            currBrand = url[0]
            print(f"Retrieving posting data for brand: {currBrand.upper()}")
        # Pause to keep the Chrome window open for 60 seconds for debugging
        time.sleep(30)
        # Close chrome driver
        driver.quit()
    

    def cg_build_custom_driver(self):
        # Launch Chrome driver with loggin disabled to clear up terminal
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3') # Suppress logs except fatal ones
        chrome_options.add_argument('--disable-logging') # Suppress logs further
        chrome_options.add_argument('--silent') # Suppress logs further
        chrome_options.add_argument(CG_HEADER_REFERRER_POLICY_STATIC)

        #chrome_options.add_argument('--headless') # No chrome window output
        # print("PRINTING CHROME DRIVER")
        # print(ChromeDriverManager().install())
        # TEMPORARY - SELENIUM ISN'T PULLING DRIVER AUTOMATICALLY
        driver_path = os.getenv("DRI_PATH")
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        
        referer = self.cg_build_base_referrer("Dodge")
        print("REFERER: " + referer)
        
        decoded_cookie = urllib.parse.unquote(CG_COOKIE)
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
            'headers': {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9',
                'cookie':  decoded_cookie,
                'dnt': '1',
                # 'referer': referer,
                'sec-ch-device-memory': '8',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.73", "Chromium";v="127.0.6533.73"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            }
        })
        # Disable navigator.webdriver
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        return driver
    
    def cg_build_URLs(self, brands):
        cgURLs = []
        for brand in brands:
            url = CG_USED_BASE_URL + CG_ORIG_ZIP \
                + self.zipcode + CG_DEF_WIDGET_TYPE \
                + CG_PRICE_FILTERS["Max Price"] + self.maxPrice \
                + CG_MILEAGE_FILTERS["Max Mileage"] + self.maxMileage \
                + CG_SORTING_DIR["Ascending"] + CG_CONTEXT \
                + CG_DISTANCE_FILTER[self.distance] \
                + CG_PRICE_FILTERS["Min Price"] + self.minPrice \
                + CG_SORTING_FILTERS["Best deals first"] \
                + CG_YEAR_FILTERS["End Year"] + self.endYear \
                + CG_MAKE_BASE + CG_MAKE_FILTERS[brand] \
                + CG_YEAR_FILTERS["Start Year"] + self.startYear
            referrerURL = self.cg_build_base_referrer(brand)
            urlPlusBrand = [brand, url, referrerURL]
            print(url)
            cgURLs.append(urlPlusBrand)
        return cgURLs
    # Every website viewing after that uses the previous URL used as the "referrer"
    # Simply typing in a URL into a blank browser makes it so there's no referer. So,
    #   everytime a URL is loaded, the next request should include the previously used URL
    def cg_build_base_referrer(self, brand):
        url = CG_USED_BASE_URL + CG_DEF_CONTEXT \
            + CG_MAKE_BASE + CG_MAKE_FILTERS[brand] \
            + CG_ZIP + self.zipcode
        return url
        