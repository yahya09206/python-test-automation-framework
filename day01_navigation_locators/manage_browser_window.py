import time

from selenium import webdriver

driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

time.sleep(2)
# make the browser window full screen
driver.fullscreen_window()

# wait
time.sleep(2)

# quit browser
driver.quit()