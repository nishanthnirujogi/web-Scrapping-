import requests
#it sends requests from local pc to amazon website
import pandas as pd
#to convert data into CSV

url = "https://www.amazon.com/s?k=LAPTOP&crid=JVP2WAYBO19Q&sprefix=laptop%2Caps%2C283&ref=nb_sb_noss_1"
# // - means whole page 
#headers for request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#HTTP Request
Webpage = requests.get(url, headers = headers)
print(Webpage)
#if you get 200 response code u can continue

Webpage.content
#this will give all the HTML code of the page
type(Webpage.content)
#to know data type

import bs4 
# we use beautiful soup to find elements in the html code 
from bs4 import BeautifulSoup
soup = BeautifulSoup(Webpage.content,"html.parser")
print(soup)
#convert the parcel into proper html file,it contails all the data

#links = soup.find_all("a",attrs={'class':'a-link-normal s-line-clamp-2 s-link-style a-text-normal'})
links = soup.find_all("a", id = 'href').get_text()
#fetch links as list 

