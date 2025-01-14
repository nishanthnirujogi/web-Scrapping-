import selenium
from selenium import webdriver
print('Imported Selenium Webdriver')

from selenium.webdriver.chrome.service import Service
path = "C:/Users/nirujogi/Desktop/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/login/")

