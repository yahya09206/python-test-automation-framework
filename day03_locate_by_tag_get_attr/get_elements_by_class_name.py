import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com/")
element_one = driver.find_element(By.CLASS_NAME, "h1y")
print(element_one.text)


# Identify first li element with class name list-group-item
first_li_item = driver.find_element(By.CLASS_NAME,"list-group-item")
print(first_li_item.text)

"""
Identify all li elements with class name list-group-item
get the size of all the elements
"""
get_all_li_items = driver.find_elements(By.CLASS_NAME, "list-group-item")
print(get_all_li_items.__sizeof__())

# Iterate over all the elements and get the text of each element
for all_items in get_all_li_items:
    print(all_items.text)

# pause for 2 seconds
time.sleep(2)

driver.quit()