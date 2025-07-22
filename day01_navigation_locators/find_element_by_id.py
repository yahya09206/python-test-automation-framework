import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


driver = webdriver.Chrome()

driver.get("https://search.yahoo.com")

search_box = driver.find_element(By.ID, "yschsp")
search_box.send_keys("Selenium", Keys.ENTER)

time.sleep(2)

driver.quit()

