import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # headless driver options
    # options = Options()
    # options.add_argument("--headless")

    # set up webdriver
    driver = webdriver.Chrome()
    driver.get("https://practice.cydeo.com/registration_form")
    yield driver
    driver.quit()

def test_error_message(driver):

    # xpath for error message
    x_path_for_error_message = "//small[.='first name must be more than 2 and less than 64 characters long']"

    string_error_element = driver.find_element(By.XPATH,x_path_for_error_message)
    print(string_error_element.is_displayed())

