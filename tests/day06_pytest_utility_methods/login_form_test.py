import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    # headless driver options
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
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

    time.sleep(2)

    success_message = driver.find_element(By.XPATH, "//div/div[@class='flash success']")

    expected_result = "You logged into a secure area!"

    assert success_message.text.startswith(expected_result)


def test_logout(driver):

    # enter credentials into form to log in
    driver.find_element(By.XPATH, "//div/input[@name='username']").send_keys("tomsmith")
    driver.find_element(By.XPATH, "//div/input[@name='password']").send_keys("SuperSecretPassword")
    driver.find_element(By.ID, "wooden_spoon").click()


    time.sleep(2)

    driver.find_element(By.XPATH, "//div/a[@href='/logout']").click()

    time.sleep(2)

    success_messages = driver.find_element(By.ID, "flash")

    expected_results = "You logged out of the secure area!"

    assert success_messages.text.startswith(expected_results)










