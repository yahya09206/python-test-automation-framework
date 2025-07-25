from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com/checkboxes")

# Identify first checkbox
checkbox_one = driver.find_element(By.ID,"box1")
print(checkbox_one.is_selected())
checkbox_one.get_attribute("checked")