# ***EXAMPLE FULL URL WITH ALL PARAMETERS SHOWING SOMETHING ***
# https://www.facebook.com/marketplace/107996279221955/vehicles?minPrice=0&maxPrice=20000
#                                                              &maxMileage=150000&maxYear=2015
#                                                              &minMileage=50000&minYear=2000
#                                                              &sortBy=creation_time_descend
#                                                              &carType=sedan%2Csuv%2Ctruck
#                                                              &topLevelVehicleType=car_truck
#                                                              &exact=false

# BELOW IS AN EXAMPLE FULLY INPUT URL. Limiting Factor - Make = Toyota
# https://www.facebook.com/marketplace/107996279221955/vehicles?minPrice=0&maxPrice=20000&maxMileage=150000&maxYear=2015&minMileage=50000&minYear=2000&sortBy=creation_time_descend&make=2318041991806363&carType=sedan%2Csuv%2Ctruck&topLevelVehicleType=car_truck&exact=false

USER = "Christopher Porter"

DEF_USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}

FB_HTML_TAGS = {"Whole Post": "x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24", #Div Class
                "Link": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lku1pv", #a
                "Image": "x9f619 x78zum5 x1iyjqo2 x5yr21d x4p5aij x19um543 x1j85h84 x1m6msm x1n2onr6 xh8yej3", #Div
                "Price": "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u", #Span
                "Description": "x1lliihq x6ikm8r x10wlt62 x1n2onr6", #Span
                "Location": "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84", #Span
                "Mileage": "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84",
                "Location&Mileage" : "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84"} # Span

FB_MAIN = "https://www.facebook.com"
FB_MP_MAIN = "https://www.facebook.com/marketplace/"
FB_MP_VEHICLES = "https://www.facebook.com/marketplace/category/vehicles/"
# 107996279221955 represents the location ID of St. Paul. Every location facebook
#       has stored has a unique location ID. They are maybe geographical coordinates
#       but unsure at this time.
FB_MP_STPAUL = "107996279221955/vehicles/?"
FB_MP_MINNEAPOLIS = "minneapolis/vehicles?"


# The url can specify what the min and max price should be for search results. The URL
#   schema seems to autofill these parameters as the first thing in the URL sequence.
PRICE_FILTERS = {"Min Price": "minPrice=",
                 "Max Price": "&maxPrice="}

MILEAGE_FILTERS = {"Min Mileage": "&minMileage=",
                   "Max Mileage": "&maxMileage="}

YEAR_FILTERS = {"Min Year": "&minYear=",
                "Max Year": "&maxYear="}

# Before any other filtering option, the user can sort the results to show specific things
#   first. In the URL schema, this parameter goes after numeric filters such as price, year, etc.
#   but goes before the vehicle "type" filter.
# DEFAULT: The website's default filter seems to be the "suggested" option if no specific option
#          is picked. Also, this option is the default sorting state if no sorting parameter is
#          given
SORTING_FILTERS = {"Suggested": "&sortBy=best_match",
                   "Price: Lowest First": "&sortBy=price_ascend",
                   "Price: Highest First": "&sortBy=price_descend",
                   "Date Listed: Newest First": "&sortBy=creation_time_descend",
                   "Date Listed: Oldest First": "&sortBy=creation_time_ascend",
                   "Distance: Nearest First": "&sortBy=distance_ascend",
                   "Distance: Furthest First": "&sortBy=distance_descend",
                   "Mileage: Lowest First": "&sortBy=vehicle_mileage_ascend",
                   "Mileage: Highest First": "&sortBy=vehicle_mileage_descend",
                   "Year: Newest First": "&sortBy=vehicle_year_descend",
                   "Year: Oldest First": "&sortBy=vehicle_year_ascend"}

# Each vehicle manufacturer seems to have a unique ID. 
MAKE_FILTERS = {"Acura": "&make=280909549507187",
                "Audi": "&make=1274042129420222",
                "Buick": "&make=436791410393181",
                "Chevy": "&make=1914016008726893",
                "Chrysler": "&make=398368117562414",
                "Dodge": "&make=402915273826151",
                "Ford": "&make=297354680962030",
                "GMC": "&make=304317923578325",
                "Honda": "&make=308436969822020",
                "Hyundai": "&make=590755841400441",
                "Jeep": "&make=408221723080125",
                "Lexus": "&make=2101813456521413",
                "Nissan": "&make=2621742507840619",
                "Ram": "&make=262465364692582",
                "Toyota": "&make=2318041991806363",
                }

DEF_BRAND_LIST = ["Dodge", "Jeep", "Chrysler"]

# Multiple body styles can be selected, resulting in a URL scheme looking like this -->
#   "&carType=minivan%2Csedan%2Csuv" instead of just "&carType=sedan"
BODYSTYLE_FILTERS = {"Base Body Style": "&carType=",
                     "Sedan-SUV-Truck": "&carType=sedan%2Csuv%2Ctruck"}

VEHICLE_TYPE_FILTERS = {"Cars & Trucks": "&topLevelVehicleType=car_truck"}


# Color Palette Constants
PRIMARY_GREEN = "#217346"
SECONDARY_GREEN = "#A9D18E"
PRIMARY_BLUE = "#1877F2"
SECONDARY_BLUE = "#E7F3FF"
DARK_GREY = "#333333"
LIGHT_GREY = "#F0F2F5"
ALERT_RED = "#FF0000"
WHITE = "#FFFFFF"