'''
Simple Web Scraper
Grabs all of the Quotes and Authors
Dec 23, 2022
Edward Naidoo 
'''

# Modules
from bs4 import BeautifulSoup
import requests
import datetime

# Variables
time = datetime.datetime.now()
page = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page.text, "html.parser")
quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

# Display
for quotes, authors in zip(quotes, authors):
    print(quotes.text + " " + authors.text + "\n")

if page:
    print("Accessed!\n")
else:
    print("Something went wrong!\n")

print(f"Pulled from 'https://quotes.toscrape.com/' at/on {time}")