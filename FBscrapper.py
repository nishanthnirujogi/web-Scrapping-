from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/login/")

username = driver.find_element_by_xpath("""/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[3]/div/div/label/div/input""")
username.send_keys("nirujogi@amazon.com")
query = "amazon reviews"
file = 0
#for i in range(1,20):
driver.get(f"https://www.tiktok.com/search/user?q={query}&t=1736861735197")
time.sleep(10)
elems = driver.find_elements(By.CLASS_NAME,"search-user-container")
print(f"{len(elems)} items found")
for elem in elems:
     d = elem.get_attribute("outerHTML")
     with open(f"tiktokurls/{query}_{file}.html", "w",encoding="utf-8") as f:
          f.write(d)
          file += 1
#print(elem.text)

time.sleep(8)
driver.close()