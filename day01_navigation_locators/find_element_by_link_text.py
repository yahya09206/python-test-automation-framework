import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()

# navigate to google
driver.get("https://google.com")

# identify search box using both name and id
searchBox = driver.find_element(By.NAME, "q")

# submit the search by clicking on the search button
searchBox.send_keys("Everything is awesome", Keys.ENTER)

# navigate back to google home page
driver.back()

# wait a few seconds
time.sleep(2)

# click on about link
driver.find_element(By.LINK_TEXT, "About").click()

# wait a few seconds
time.sleep(2)

# quit browser
driver.quit()
