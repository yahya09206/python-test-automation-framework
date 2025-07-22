import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com/")

# get the first link on the page and get href attribute
first_link = driver.find_element(By.LINK_TEXT, "A/B Testing")

# get any attribute of identified element, in this case href
print(first_link.get_attribute("href"))

time.sleep(2)

driver.close()