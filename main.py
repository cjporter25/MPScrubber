# New System move - 4.15.24 - Christopher J. Porter

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Marketplace Imports

from marketplaceFB.facebookMP_GUI import *


input = input("Running MAIN(1) or Dev-GUI(2)? --> ")

if input == "2":
    app = QApplication(sys.argv)
    window = ScrubberGUI()
    window.show()
    sys.exit(app.exec_())

#**********************MOCK USER INPUT**********************#
# prefMinPrice = 0
# prefMaxPrice = 20000
# prefMinMiles = 50000
# prefMaxMiles = 100000
# prefMinYear = 2000
# prefMaxYear = 2015
# prefSorting = SORTING_FILTERS["Date Listed: Newest First"] # Covered by the statement: SORTING_FILTERS["Date Listed: Newest First"]
# prefBodyStyles = BODYSTYLE_FILTERS["Sedan-SUV-Truck"] # "&carType=sedan%2Csuv%2Ctruck"
# prefVehicleType = VEHICLE_TYPE_FILTERS["Cars & Trucks"]
#**********************MOCK USER INPUT**********************#


# Build a list of URLS to access for each brand
# prefBrands = ["Chevy", "Toyota", "Ford", "Lexus", "Dodge"]
prefBrands = ["Chevy", "Toyota"]
fb = facebookMP()
urls = fb.build_URLs(prefBrands)
newDate = fb.get_current_date_and_time()
print(newDate)
# Launch Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)

#****************************Main Scrubber Driver*********************************#

# Open each URL 
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
        continue

    # url[0] contains a string of the current brand being looked at
    currBrand = url[0]

    print("Retrieving posting data...")
    newEntries = fb.retrieve_postings(page_source)
    print("Creating or initializing table for " + currBrand.upper() + "...")
    fb.create_table(currBrand)
    print("Inserting new entries...")
    fb.insert_entries(currBrand, newEntries)
    # fb.show_table_ordered(currBrand, "DatePulled")
    print("Current total: " + fb.get_row_count(currBrand))
    fb.wait()
#****************************Main Scrubber Driver*********************************#

# Close chrome driver
driver.quit()

#****************************Generate Excel Report*********************************#
rm = ReportsManager()
rm.set_primary_directory()
rm.build_new_report(prefBrands, 10)
#****************************Generate Excel Report*********************************#