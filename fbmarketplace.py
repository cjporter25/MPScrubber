# ***EXAMPLE FULL URL WITH ALL PARAMETERS SHOWING SOMETHING ***
# https://www.facebook.com/marketplace/107996279221955/vehicles?minPrice=0&maxPrice=20000
#                                                              &maxMileage=150000&maxYear=2015
#                                                              &minMileage=50000&minYear=2000
#                                                              &sortBy=creation_time_descend
#                                                              &carType=sedan%2Csuv%2Ctruck
#                                                              &topLevelVehicleType=car_truck
#                                                              &exact=false



# Before anything other filtering option, the user can sort the results to show specific things
#   first. In the URL schema, this parameter goes after numeric filters such as price, year, etc.
#   but goes before the vehicle "type" filter.
# DEFAULT: The website's default filter seems to be the "suggested" option if no specific option
#          is picked. Also, this option is the default sorting state if no sorting parameter is
#          given
SORTING_FILTERS = {"Suggested": "&sortBy=best_match",
                   "Price: Lowest first": "&sortBy=price_ascend",
                   "Price: Highest first": "&sortBy=price_descend",
                   "Date Listed: Newest first": "&sortBy=creation_time_descend",
                   "Date Listed: Oldest first": "&sortBy=creation_time_ascend",
                   "Distance: Nearest first": "&sortBy=distance_ascend",
                   "Distance: Furthest first": "s&ortBy=distance_descend",
                   "Mileage: Lowest first": "&sortBy=vehicle_mileage_ascend",
                   "Mileage: Highest first": "&sortBy=vehicle_mileage_descend",
                   "Year: Newest first": "&sortBy=vehicle_year_descend",
                   "Year: Oldest first": "&sortBy=vehicle_year_ascend"}

# The url can specify what the min and max price should be for search results. The URL
#   schema seems to autofill these parameters as the first thing in the URL sequence.
PRICE_FILTERS = {"Min Price": "minPrice=",
                 "Max Price": "maxPrice="}

# Each vehicle manufacturer seems to have a unique ID. 
MAKE_FILTERS = {"Chevy": "&make=1914016008726893",
                "Dodge": "&make=402915273826151",
                "Honda": "&make=308436969822020",
                "Ford": "&make=297354680962030",
                "Lexus": "&make=2101813456521413",
                "Toyota": "&make=2318041991806363",
                }

YEAR_FILTERS = {"Min Year": "&minYear=",
                "Max Year": "&maxYear="}

VEHICLE_TYPE_FILTERS = {"Cars & Trucks": "&topLevelVehicleType=car_truck"}

MILEAGE_FILTERS = {"Min Mileage": "&minMileage=",
                   "Max Mileage": "&maxMileage="}

# Multiple body styles can be selected, resulting in a URL scheme looking like this -->
#   "&carType=minivan%2Csedan%2Csuv" instead of just "&carType=sedan"
BODYSTYLE_FILTERS = {"Base Body Style": "&carType="}

