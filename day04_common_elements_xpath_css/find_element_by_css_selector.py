import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://search.yahoo.com")

# Identify yahoo search box using CssSelector

# Can't get text using cssSelector

# Wait a little bit
time.sleep(3)

# Clear text from searchBox

# Type in XPATH into searchBox

# Click submit

# Wait a little bit
time.sleep()

# quit driver
driver.quit()