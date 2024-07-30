
# EXAMPLE FULL URL:
# https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=55343
# &inventorySearchWidgetType=AUTO
# &maxPrice=80000
# &maxMileage=30000
# &priceDropsOnly=true
# &sortDir=ASC
# &sourceContext=carGurusHomePageModel
# &distance=50
# &ratings=1            <- "Great deal" was selected
# &ratings=2            <- "Good deal" was selected
# &minPrice=3000
# &sortType=DEAL_SCORE
# &endYear=2023
# &entitySelectingHelper.selectedEntity=m24
# &startYear=2010


CG_HEADER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
CG_HEADER_ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
CG_HEADER_ACCEPT_ENCODING = 'gzip, deflate, br, zstd'
CG_HEADER_ACCEPT_LANGUAGE = 'en-US,en;q=0.9'

# Used when URL is pasted in directly, i.e., opening a link from an email
CG_HEADER_REFERRER_POLICY_STATIC = '--referrer-policy=strict-origin-when-cross-origin'
CG_HEADER_SEC_FETCH_STATIC = '--sec-fetch-site=none'

# Used when the website recognizes a slight change of filters and was reloaded
CG_HEADER_REFERRER_POLICY_LOCAL = '--referrer-policy=origin-when-cross-origin'
CG_SEC_FETCH_SITE = 'same-origin'

CG_HEADER_USER = '--sec-fetch-user=?1'


CG_HTML_TAGS = {"Whole Post": "pazLTN", # div
                "Link": "Z0_BC0 ZGMXbN kKD2eQ", # a
                "Post Data Wrapper": "k4FSCT", # div
                "Post Data": "z6DN8 BVBRBZ", # div
                "Description Chunk": "TaYD- bLgDNy", # div
                "Description Text": "gN7yGT", # h4
                "Mileage, Engine, Price": "YlkCzk", # div
                "Mileage, Engine": "Eeli0s", # div
                "Mileage": "Hczm1C", # p 
                "Engine": "coushe", # p
                "Price & Deal": "Lxkk9T", #div
                "Price": "ulx4Y8", #h4
                }

CG_USED_BASE_URL = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?"

# Removed the "&". This piece will be set to always follor the BASE URL.
CG_WIDGET_TYPE = "inventorySearchWidgetType=AUTO"
CG_DEF_WIDGET_TYPE = "&inventorySearchWidgetType=AUTO"

# The "context" is also consistent and will go immediately after the widget type
CG_CONTEXT = "&sourceContext=carGurusHomePageModel"

CG_DEF_CONTEXT = "sourceContext=carGurusHomePageModel"

CG_PRICE_FILTERS = {"Min Price": "&minPrice=",
                    "Max Price": "&maxPrice=",}

CG_YEAR_FILTERS = {"Start Year": "&startYear",
                   "End Year": "&endYear=",}

# No "min" mileage. The filter only shows the selected amount or lower.
# Default - doesn't show or = "any"
CG_MILEAGE_FILTERS = {"Max Mileage": "&maxMileage=",}

# EVery make uses this helper entity, but has its own dedicated value
CG_MAKE_BASE = "&entitySelectingHelper.selectedEntity="

# Changing this value in the URL does affect what is displayed
# NO DEFAULT
CG_MAKE_FILTERS = {"Acura": "m4",
                   "Audi": "m19",
                   "Buick": "m21",
                   "Cadillac": "m22",
                   "Chevrolet": "m1",
                   "Chrysler": "m23",
                   "Dodge": "m24",
                   "Jeep": "m32",}

# Sort direction determines ascending or descending. Sort type determines
#       what element to sort
# DEFAULT IS BEST MATCH. 
CG_SORTING_DIR = {"Ascending": "&sortDir=ASC", # "Lowest" something first
                  "Descending": "&sortDir=DESC",# "Highest" something first
                 } 
CG_SORTING_FILTERS = {"Best match": "&sortType=BEST_MATCH",
                    "Best deals first": "&sortType=DEAL_SCORE",
                    "Worst deals first": "&sortType=DEAL_SCORE",
                    "Lowest price first": "&sortType=PRICE",
                    "Highest price first": "&sortType=PRICE",
                    "Lowest mileage first": "&sortType=MILEAGE",
                    "Highest mileage first": "&sortType=MILEAGE",
                    "Newest first (by car year)": "sortType=NEWEST_CAR_YEAR",
                    "Oldest first (by car year)": "sortType=NEWEST_CAR_YEAR",
                    "Closest first": "sortType=PROXIMITY",
                    "Furthest first": "sortType=PROXIMITY",
                    "Newest listings first": "sortType=AGE_IN_DAYS",
                    "Oldest listing first": "sortType=AGE_IN_DAYS",}
CG_SORTING_FILTERS_FULL = {"Best match": "&sortType=BEST_MATCH",
                        "Best deals first": "&sortDir=ASC&sortType=DEAL_SCORE",
                        "Worst deals first": "&sortDir=DESC&sortType=DEAL_SCORE",
                        "Lowest price first": "&sortDir=ASC&sortType=PRICE",
                        "Highest price first": "&sortDir=DESC&sortType=PRICE",
                        "Lowest mileage first": "&sortDir=ASC&sortType=MILEAGE",
                        "Highest mileage first": "&sortDir=DESC&sortType=MILEAGE",
                        "Newest first (by car year)": "&sortDir=ASC&sortType=NEWEST_CAR_YEAR",
                        "Oldest first (by car year)": "&sortDir=DESC&sortType=NEWEST_CAR_YEAR",
                        "Closest first": "&sortDir=ASC&sortType=PROXIMITY",
                        "Furthest first": "&sortDir=DESC&sortType=PROXIMITY",
                        "Newest listings first": "&sortDir=ASC&sortType=AGE_IN_DAYS",
                        "Oldest listing first": "&sortDir=DESC&sortType=AGE_IN_DAYS",}

# Multiple inputs of the "ratings" parameter will select each of their respective 
#   boxes.
CG_DEAL_RATING = {"Great Deal": "&ratings=1",
                  "Good Deal": "&ratings=2",
                  "Fair Deal": "&ratings=3",}

CG_PRICE_DROPS_ONLY = {"Price drops": "&priceDropsOnly=true"}

# Calculated as radius from provided zip code. Changing this value in the URL
#   does affect what is displayed
# DEFAULT = 50
CG_DISTANCE_FILTER = {"10": "&distance=10",
                      "25": "&distance=25",
                      "50": "&distance=50",
                      "75": "&distance=100",
                      "100": "&distance=100",
                      "150": "&distance=150",
                      "200": "&distance=200",
                      "500": "&distance=500",}
CG_ZIP = "&zip="
CG_ORIG_ZIP = "zip="


DEF_ZIP = "55401"
DEF_DISTANCE = "50"
DEF_BRAND_ONE = ["Dodge"]
DEF_BRAND_LIST = ["Dodge", "Jeep", "Chrysler"]


CG_COOKIE = 'CarGurusUserT=DUm1-73.62.144.117_1722020584373; ViewVersion=%7B%22en%22%3A%7B%22exclude%22%3A%7B%227bf01801-3707-433d-b5c9-35e3ac9fe5b7%22%3A1%7D%2C%22type%22%3A%22OUT%22%7D%7D; MultivariateTest=H4sIAAAAAAAAAKtWcvVz9%2FEM9lCyqlYyMzVTslIysDZQ0lEyszQCsnUNQUwLcyDT0MzEDCxuBhM3MTIFiRsYG4MVWcD1moLZhiZG5kq1tQArgXsnYgAAAO7%2B%2FvNgiOU5SuEfEDpkCquRwk%2F0ae1zdLaENDuVpzhb; usprivacy=1YNN; mySavedListings=%7B%22id%22%3A%2214799961-4648-42d6-8dc4-09c61f45425d%22%7D; OTGPPConsent=DBABLA~BVQVAAAABgA.QA; LPVID=M4ODNiZTdhMjg1NWM3MDcw; _sp_ses.df9a=*; LSW=www-i-0fc60ebba30cb1dc5; baseZip_asOf=55345_1722126181890; preferredContactInfo=Y2l0eT1NaW5uZWFwb2xpcypwb3N0YWxDb2RlPTU1NDAxKnN0YXRlPU1OKmNvdW50cnk9VVMqaG9tZVBvc3RhbENvZGU9NTU0MDEq; JSESSIONID=F61E7CE1C3F425D3B48480182CE6588C; cg-ssid=1911b5e956a0cdeff81e80bda5a7144c344b91767c7b53628b8008109b4aadb2; pastListingSearches="{@s@:@USED@,@d@:50,@t@:1722139200000,@z@:@55401@,@l@:@en@}/{@s@:@USED@,@d@:50,@t@:1722139200000,@e@:@m24@,@z@:@55401@,@l@:@en@}/{@s@:@USED@,@d@:50,@t@:1722139200000,@e@:@m32@,@y2@:2024,@z@:@55401@,@l@:@en@}/{@s@:@USED@,@d@:50,@t@:1722139200000,@e@:@m2@,@y1@:2010,@z@:@55343@,@l@:@en@}/{@s@:@USED@,@d@:150,@t@:1722139200000,@e@:@m23@,@y1@:2010,@y2@:2024,@z@:@55343@,@l@:@en@}/{@s@:@NEW@,@d@:150,@t@:1722139200000,@e@:@m23@,@y1@:2010,@y2@:2024,@z@:@55343@,@l@:@en@}/"; datadome=3S27NH3GKCZ5_zR9XaPg4jH4eHQXM_xMTmWyUn5tlF2MeXRIrZSvWxV4ihRhgoIi85cL4pMbjw2qa1hFBBGLEPKVzTYkox29OnGIk5Cf0gdiPE9DjA4k7tU1ZMbeMzLj; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jul+27+2024+23%3A07%3A44+GMT-0500+(Central+Daylight+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9afeb3d6-c775-4c6f-816f-9a5090f84286&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&GPPCookiesCount=1&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false; _sp_id.df9a=e963c4c7-5a6a-468f-978d-8f80143e3cbb.1722020585.4.1722139670.1722049417.3f11ab11-a7d3-4633-9dad-62ad3113dd8a'

CUSTOM_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': "Cookie",
    'Referer': 'https://example.com',
    'Dnt': '1',
    'Priority': 'u=0, i',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.73", "Chromium";v="127.0.6533.73"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}