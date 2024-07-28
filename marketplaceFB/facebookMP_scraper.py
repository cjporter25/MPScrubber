import os

from bs4 import BeautifulSoup

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from marketplaceFB.facebookMP_database import *
from mpsTools.util import *

class FB_Scrapper:
    def __init__(self, minYear="2000", maxYear="2024", minPrice="0", 
                 maxPrice="50000", minMiles="0", maxMiles="250000",
                 brands=None, location=None, sorting=None, 
                 bodyStyles=None, vehicleTypes=None):
        self.minYear = minYear
        self.maxYear = maxYear
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.minMiles = minMiles
        self.maxMiles = maxMiles
        self.brands = brands if brands is not None else DEF_BRAND_LIST
        self.location = location if location is not None else FB_MP_STPAUL
        self.sorting = sorting if sorting is not None else FB_SORTING_FILTERS["Date Listed: Newest First"]
        self.bodyStyles = bodyStyles if bodyStyles is not None else BODYSTYLE_FILTERS["Sedan-SUV-Truck"]
        self.vehicleTypes = vehicleTypes if vehicleTypes is not None else VEHICLE_TYPE_FILTERS["Cars & Trucks"]
    def scrape(self):
        newDate = get_formatted_date_and_time()
        print(f"Current date and time: {newDate}")
        fbURLs = self.fb_build_URLs(self.brands)
        db = FB_DatabaseManager()

        # Launch Chrome driver
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3') # Suppress logs except fatal ones
        chrome_options.add_argument('--disable-logging') # Suppress logs further
        chrome_options.add_argument('--silent') # Suppress logs further
        chrome_options.add_argument('--headless') # No chrome window output
        # print("PRINTING CHROME DRIVER")
        # print(ChromeDriverManager().install())
        # TEMPORARY - SELENIUM ISN'T PULLING DRIVER AUTOMATICALLY
        driver_path = os.getenv("DRI_PATH")
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        wait = WebDriverWait(driver, 5)

        # Open each URL 
        for url in fbURLs:
            try:
                # url[1] contains the actual built URL
                driver.get(url[1]) #Get the URL's data
                get_url = driver.current_url #Retrieve what the driver used as the URL
                wait.until(EC.url_to_be(url[1])) #Wait to let the page load
                if get_url == url[1]:    #If the used URL matches the original, grab the page source
                    page_source = driver.page_source
            except Exception as e:
                print(f"Error occurred while loading URL {url[1]}: {e}")
                continue

            # url[0] contains a string of the current brand being looked at
            currBrand = url[0]
            print(f"Retrieving posting data for brand: {currBrand.upper()}")

            newEntries = self.retrieve_postings(page_source)
            db.create_table(currBrand)
            db.insert_entries(currBrand, newEntries)
            db.show_brand_meta_data(currBrand)
            pause()

        # Close chrome driver
        driver.quit()

    def fb_build_URLs(self, brands):
        fbURLs = []
        for brand in brands: 
            url = FB_MP_MAIN + self.location \
                    + FB_PRICE_FILTERS["Min Price"] + self.minPrice \
                    + FB_PRICE_FILTERS["Max Price"] + self.maxPrice \
                    + FB_MILEAGE_FILTERS["Min Mileage"] + self.minMiles \
                    + FB_MILEAGE_FILTERS["Max Mileage"] + self.maxMiles \
                    + FB_YEAR_FILTERS["Min Year"] + self.minYear \
                    + FB_YEAR_FILTERS["Max Year"] + self.maxYear \
                    + self.sorting + FB_MAKE_FILTERS[brand] \
                    + self.bodyStyles + self.vehicleTypes
            urlPlusBrand = [brand, url]
            print(urlPlusBrand)
            fbURLs.append(urlPlusBrand)
        return fbURLs
    
    def retrieve_postings(self, page_source):
        dbEntries = []
        soup = BeautifulSoup(page_source, features= "html.parser") 
        # Find all postings that are containerized with the following HTML class tag
        postings = soup.body.find_all('div', class_ =  FB_HTML_TAGS["Whole Post"])
        count = 0
        for post in postings:
            if count == 15: #Limit 10 posts at a time
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
            price = convert_to_int(post.find('span', class_ = FB_HTML_TAGS["Price"]).text)
            # Location and mileage use the same HTML tag for some stupid reason
            locAndMile = post.find_all('span', class_ = FB_HTML_TAGS["Location&Mileage"])
            # The first one is mileage in the format of "55k" or "100k". Remove the letters,
            #   convert to int, and multiply by a 1000 to get the actual number.
            mileage = (convert_to_int(locAndMile[1].text)) * 1000
            # The second one is location, simply convert to text
            location = locAndMile[0].text
            
            # Create a primary key for the entry
            primaryKey = create_primary_key(year, price, mileage)

            datePulled = get_formatted_date_and_time()

            # NOTE: Will eventually look work a way to pull the approx time a vehicle was posted
            datePosted = "n/a"

            # Create a new entry tuple. Primary key will always be first item
            newEntry = (primaryKey, datePulled, datePosted, year, price, mileage, desc, location, fullLink)
            dbEntries.append(newEntry)
            count+=1
        return dbEntries








                





