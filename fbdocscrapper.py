from csv import writer
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import random
import pandas as pd
import numpy as np



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")

driver.maximize_window()

email_element=driver.find_element(By.ID,"email")
password_element=driver.find_element(By.ID,"pass")

email_element.send_keys("topgunmaverick392@gmail.com")
password_element.send_keys("nani1408@")

login_button=driver.find_element(By.NAME,'login')
login_button.click()

#random delay to avoid suspected bot activity on the platform
delay = random.uniform(4, 7)
time.sleep(delay)

search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search Facebook"]')
search_bar.send_keys('Amazon no review')
search_bar.send_keys(Keys.RETURN)


delay = random.uniform(4, 7)
time.sleep(delay)



sc=1
while sc<7:
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 delay = random.uniform(4, 7)
time.sleep(delay)
sc+= 1

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

links=soup.find_all("a",href=True)

groups=[]

for link in links:
 group_name=link.get_text(strip=True)
 group_link=link["href"]
 groups.append({"name":group_name,"link":group_link})

delay = random.uniform(4, 7)
time.sleep(delay)

groups_data=pd.DataFrame(groups)

groups_data["name"][0]

groups_data["Flag"]=np.where(groups_data["link"].str.contains("/groups/"),1,0)
groups_data["Flag"]=np.where(groups_data["link"].str.contains("=%3C"),0,groups_data["Flag"])

groups_data_final=groups_data[groups_data["Flag"]==1]

groups_data_final.sort_values(by=['link','name'],inplace=True)
groups_data_final.drop_duplicates(subset=["link"],inplace=True)

#CHANGE THE PATH TO HAVE THE GET URLS LIST
groups_data_final.to_excel(r"C:\Users\nirujogi\Desktop\Scrapper_Extract_Files\FB Scraper Assigns\Rawdump\Review.xlsx",index=False)

# ONCE ABOVE SCRIPT IS RUN THE URLS LIST WILL GET GENERATED.

groups_data_final
