import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    # headless driver options
    options = Options()
    options.add_argument("--headless") # comment out to see browser

    # set up webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_website_title(driver):

    driver.get("https://practice.cydeo.com")
    expected_title = "Practice"

    actual_title = driver.title

    assert actual_title == expected_title, f"Expected '{expected_title}' but got '{actual_title}'"

def test_yahoo_title(driver):





