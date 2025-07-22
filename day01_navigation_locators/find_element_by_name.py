"""
# Launch Chrome

chrome_driver = webdriver.Chrome()

chrome_driver.get('https://bstackdemo.com/')

print("Title in Chrome:", chrome_driver.title)

chrome_driver.quit()
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://search.yahoo.com")

search_box = driver.find_element(By.NAME, "p")
# type search term and press enter
search_box.send_keys("Selenium", Keys.ENTER)


time.sleep(2)

driver.quit()

