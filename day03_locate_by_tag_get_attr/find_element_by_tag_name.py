from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://practice.cydeo.com")

first_link = driver.find_element(By.TAG_NAME, "a")
print(first_link.text)