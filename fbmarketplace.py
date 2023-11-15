
# Before anything other filtering option, the user can sort the results to show specific things
#   first. In the URL schema, this parameter goes after numeric filters such as price, year, etc.
#   but goes before the vehicle "type" filter.
# DEFAULT: The website's default filter seems to be the "suggested" option if no specific option
#          is picked.
SORTING_FILTERS = {"Suggested": "sortBy=best_match",
                   "Price: Lowest first": "sortBy=price_ascend",
                   "Price: Highest first": "sortBy=price_descend",
                   "Date Listed: Newest first": "sortBy=creation_time_descend",
                   "Date Listed: Oldest first": "sortBy=creation_time_ascend",
                   "Distance: Nearest first": "sortBy=distance_ascend",
                   "Distance: Furthest first": "sortBy=distance_descend",
                   "Mileage: Lowest first": "sortBy=vehicle_mileage_ascend",
                   "Mileage: Highest first": "sortBy=vehicle_mileage_descend",
                   "Year: Newest first": "sortBy=vehicle_year_descend",
                   "Year: Oldest first": "sortBy=vehicle_year_ascend"}

PRICE_FILTERS = {"Min Price": "minPrice=",
                 "Max Price": "maxPrice="}

