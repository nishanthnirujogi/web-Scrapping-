from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=PRO6S7TYSC47&sprefix=laptop%2Caps%2C287&ref=nb_sb_noss_2")
elem = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))


time.sleep(8)
driver.close()