import time
import random
import requests
import json
import datetime
from datetime import date

###### HELPER METHODS ######
# 
def brand_name_upper_case(brand):
    ucBrand = brand.upper()
    return ucBrand

def pause():
    print("Automated Detection System Prevention. Waiting before scrapping the next brand...")
    random_number = random.randint(2, 8)
    for i in range(random_number, 0, -1):
        print("...")
        time.sleep(1)

def long_pause():
    print("Automated Detection System Prevention. Waiting before scrapping the next brand...")
    random_number = random.randint(10, 30)
    for i in range(random_number, 0, -1):
        print("...")
        time.sleep(1)
def get_formatted_date_and_time():
    today = date.today()
    currDate = today.strftime("%Y-%m-%d")
    time = datetime.datetime.now().time()
    currTime = time.strftime("%H:%M:%S")
    currDateTime = currDate + "." + currTime
    return currDateTime
def convert_to_int(newString):
    if newString == "FREE" or newString == "Free":
        return 0
    if newString == None:
        return 0
    try:
        # Create new numeric string by removing non-digits
        numericString = ''.join(c for c in newString if c.isdigit())
        # Type cast to Int
        value = int(numericString)
        return value
    except ValueError as e:
        errorPart = newString[e.args[0]:e.args[1]] if isinstance(e.args, tuple) and len(e.args) == 2 else None
        result = {'error': 'ValueError', 'message': str(e), 'entire_string': newString, 'error_part': errorPart}
        print("Error occurred during extraction:")
        print("Type:", result['error'])
        print("Message:", result['message'])
        print("Entire string:", result['entire_string'])
        print("Error part:", result['error_part'])
        return 0
def create_primary_key(year, price, mileage):
    uniqueID = "{}-{}-{}".format(year, price, mileage)
    return uniqueID
