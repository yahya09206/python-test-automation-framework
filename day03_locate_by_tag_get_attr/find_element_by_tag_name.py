import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com")

first_link = driver.find_element(By.TAG_NAME, "a")
print(first_link.text)

time.sleep(2)

driver.quit()