from bs4 import BeautifulSoup
import requests 
import os

from clmp import *
from fbmp import *

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
                              
print("URL in use: " + fburl)
page_html = requests.get(fburl) 
print(page_html)

scrubber = BeautifulSoup(page_html.text, "html.parser")
print(scrubber.get_text())