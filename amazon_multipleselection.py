from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
query = "laptop"
file = 0
for i in range(1,20):
 driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=PRO6S7TYSC47&sprefix=laptop%2Caps%2C287&ref=nb_sb_noss_2")

 elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
 print(f"{len(elems)} items found")
 for elem in elems:
     d = elem.get_attribute("outerHTML")
     with open(f"data/{query}_{file}.html", "w",encoding="utf-8") as f:
          f.write(d)
          file += 1
#print(elem.text)

 time.sleep(8)
driver.close()