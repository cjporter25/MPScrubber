# New System move - 4.15.24 - Christopher J. Porter
import sys
import threading
import csv
import time
import psutil

# Marketplace Imports
from marketplaceFB.facebookMP_GUI import *
from marketplaceFB.facebookMP_performance import *


firstInput = input("Running Demo(1) or Dev-GUI(2)? --> ")

if (firstInput == "1"):
    secondInput = input("Are you sure? This demo will take roughly 30 seconds to complete. If you are sure press (Y/y) for yes or (N/n) for no: ")
    if secondInput == "N" or secondInput == "n":
        print("Switching to GUI mode")
        print("Okay! Opening the example GUI instead. Rerun the application to run the demo if you'd like.")
        firstInput = "2"

if (firstInput == "2"):
    app = QApplication(sys.argv)
    window = ScrubberGUI() 
    # Set the window to stay on top
    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()

    # Bring the window to the front
    window.raise_()
    window.activateWindow()

    # Reset the window flags to default so it doesn't always stay on top
    # after it gains focus
    window.setWindowFlags(window.windowFlags() & ~Qt.WindowStaysOnTopHint)
    window.show()   
    sys.exit(app.exec_())


# Start network monitoring
start_network_monitoring()


# Build a list of URLS to access for each brand
#prefBrands = ["Chevy", "Toyota", "Ford", "Lexus", "Dodge"]
# prefBrands = ["Lexus", "Toyota", "Ford"]
prefBrands = ["Chevy", "Toyota"]
fb = FB_Scrapper()
db = FB_DatabaseManager()
prefBrands = sorted(prefBrands)
urls = fb.build_URLs(prefBrands)
newDate = fb.get_current_date_and_time()
print(f"Current date and time: {newDate}")


# Launch Chrome driver
chrome_options = Options()
chrome_options.add_argument('--log-level=3') # Suppress logs
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--silent')
# chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--headless') 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 5)

#****************************Main Scrapper Driver*********************************#

# Open each URL 
for url in urls:
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

    newEntries = fb.retrieve_postings(page_source)
    db.create_table(currBrand)
    db.insert_entries(currBrand, newEntries)
    db.show_brand_meta_data(currBrand)
    db.wait()

# Close chrome driver
driver.quit()

#****************************Generate Excel Report*********************************#
rm = ReportsManager()
rm.build_new_report(prefBrands, 15)
#****************************Generate Excel Report*********************************#



