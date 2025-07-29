import time

from selenium import webdriver

"""
from selenium import webdriver

# Launch Chrome

chrome_driver = webdriver.Chrome()

chrome_driver.get('https://bstackdemo.com/')

print("Title in Chrome:", chrome_driver.title)

chrome_driver.quit()

"""
# launch chrome
chrome_driver = webdriver.Chrome()

chrome_driver.get("https://google.com")

print("Title in Chrome:", chrome_driver.title)

# sleep for 2 seconds
time.sleep(2.0)

chrome_driver.quit()


