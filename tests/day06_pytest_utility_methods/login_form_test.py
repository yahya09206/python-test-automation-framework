import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.get("https://practice.cydeo.com/login")
    yield driver
    driver.quit()

def test_login(driver):

    # locate header element
    header = driver.find_element(By.XPATH, "//h2[.='Login Page']")
    # get header element text
    print(header.text)

    # enter credentials into form
    driver.find_element(By.XPATH, "//div/input[@name='username']").send_keys("tomsmith")
    driver.find_element(By.XPATH, "//div/input[@name='password']").send_keys("SuperSecretPassword")
    driver.find_element(By.ID, "wooden_spoon").click()





