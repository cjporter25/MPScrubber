from bs4 import BeautifulSoup
import requests 
import os

TEST_URL = "https://quotes.toscrape.com/"
FB_MP_MAIN = "https://www.facebook.com/marketplace/"
FB_MP_VEHICLES = "https://www.facebook.com/marketplace/category/vehicles/"
FB_MP_VEHICLES_STPAUL = "https://www.facebook.com/marketplace/107996279221955/vehicles"


webpage_html = requests.get(TEST_URL)
soup = BeautifulSoup(webpage_html.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)