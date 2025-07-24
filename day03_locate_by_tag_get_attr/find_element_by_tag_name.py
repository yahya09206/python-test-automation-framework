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

# find element by tag name
first_link = driver.find_element(By.TAG_NAME, "a")
print(first_link.text)

all_links = driver.find_elements(By.TAG_NAME, "a")

time.sleep(2)

# get all elements with a tag name of a and print their text and attribute
all_links_on_page = driver.find_elements(By.TAG_NAME, "a")
print(all_links_on_page.__sizeof__())

for allLinks in all_links_on_page:
    print(allLinks.text)
    print(allLinks.get_attribute("href"))

time.sleep(2)

#Get first element with <h1> tag and get the text out of it
first_h1_tag_element = driver.find_element(By.TAG_NAME, "h1")
print(first_h1_tag_element.text)
driver.quit()