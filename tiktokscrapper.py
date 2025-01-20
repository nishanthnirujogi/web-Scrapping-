from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
query = "amazon 5 reviews"
file = 0
#for i in range(1,20):

driver.get(f"https://www.tiktok.com/search/user?q={query}&t=1736861735197")

elems = driver.find_elements(By.CLASS_NAME,"search-user-container")
print(f"{len(elems)} items found")
for elem in elems:
     d = elem.get_attribute("outerHTML")
     with open(f"tiktokurls/{query}_{file}.html", "w",encoding="utf-8") as f:
          f.write(d)
          file += 1
#print(elem.text)

delay = random.uniform(4, 7)
time.sleep(delay)
driver.close()