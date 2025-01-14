from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/login/")
time.sleep(10)
