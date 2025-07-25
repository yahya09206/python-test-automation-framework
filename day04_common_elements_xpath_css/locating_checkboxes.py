import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com/checkboxes")

# Identify first checkbox
checkbox_one = driver.find_element(By.ID,"box1")
print(checkbox_one.is_selected())
checkbox_one.get_attribute("checked")

# Identify second checkbox
checkbox_two = driver.find_element(By.ID,"box2")
print(checkbox_two.is_selected())
checkbox_two.get_attribute("checked")

# Click box_one to check it
checkbox_one.click()
print(checkbox_one.is_selected())
# Click box_two to uncheck it
checkbox_two.click()
print(checkbox_two.is_selected())

# If box one is not selected, then check it
# Else, display "already checked"
if checkbox_one is not checkbox_one.is_selected():
    checkbox_one.click()
else:
    print("Take it easy, already checked")


# If box two is not selected then check
# Else, display "already checked"
if checkbox_two is not checkbox_two.is_selected():
    checkbox_two.click()
else:
    print("Take it easy, already checked")

time.sleep(3)

driver.quit()