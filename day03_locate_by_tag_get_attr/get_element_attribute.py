from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# Navigate to google.com and identify the search box and get couple attribute values
driver.get("https://google.com")

# identify search box element
search_box = driver.find_element(By.NAME, "q")

# Get the class attribute
print(search_box.get_attribute("class"))

# Get the maxlength attribute
print(search_box.get_attribute("maxlength"))
