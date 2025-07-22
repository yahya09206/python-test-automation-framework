import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# navigate to https://practice.cydeo.com/
driver.get("https://practice.cydeo.com/")

# get all the links that have partial text A in it
all_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "A")

# get the size of this list so we know how many links with partial text A
print(all_links.__sizeof__())

# get the first item and get the text
first_item = all_links[1]
print(first_item.text)

# iterate over the whole list and print out the text
for elements in all_links:
    print(elements.text)

time.sleep(2)

# quit
driver.quit()
