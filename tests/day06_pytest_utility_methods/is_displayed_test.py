import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    # headless driver options
    options = Options()
    options.add_argument("--headless")

    # set up webdriver
    driver = webdriver.Chrome()
    driver.get("https://practice.cydeo.com/registration_form")
    yield driver
    driver.quit()