from bs4 import BeautifulSoup
import requests 
import os

import logging
import random
import re
import sqlite3
import time
import asyncio

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
                              

response = requests.get(fburl) 
print(response.url)
print(response.status_code)
#print(response.headers)
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
#posts = scrubber.find_all('div', class_='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e xnpuxes x291uyu x1uepa24 x1iorvi4 xjkvuk6')
print(soup.find("title"))

description_list = soup.find_all("span", class_ =  FB_HTML_TAGS["Description"])
print(FB_HTML_TAGS["Description"])
for item in description_list:
    print(item.text)

#for uPost in posts:
#    try:
#        image = uPost.find('img', class_='xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3')['src']
#        title = uPost.find('span', 'x1lliihq x6ikm8r x10wlt62 x1n2onr6').text
#        price = uPost.find('span', 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u').text
#        url = uPost.find('a', class_='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lku1pv')['href']
#        print(f"Image: {image}")
#        print(f"Price: {price}")
#        print(f"Title: {title}")
#    except:
#        pass



#posts = scrubber.findAll("span", attrs={"class":"text"})
#print(posts)
#for info in posts:
   # print(info.text)