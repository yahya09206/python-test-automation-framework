import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# navigate to practice site's forgot_password page
driver.get("https://practice.cydeo.com/forgot_password")


# locate two elements using css selector and enter email
email_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
email_box.send_keys("someone@someone.com")

time.sleep(2)
# locate and click retrieve button
driver.find_element(By.XPATH, "//button[@id='form_submit']").click()

time.sleep(2)

driver.quit()