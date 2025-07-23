import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
         * Purple tagname
         * Orange att name
         * Blue att value
         * Black text value
         

"""
driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com")

first_link = driver.find_element(By.TAG_NAME, "a")
print(first_link.text)

all_links = driver.find_elements(By.TAG_NAME, "a")



time.sleep(2)

driver.quit()