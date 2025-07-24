import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com/")
element_one = driver.find_element(By.CLASS_NAME, "h1y")
print(element_one.text)


# Identify first li element with class name list-group-item


time.sleep(2)

driver.quit()