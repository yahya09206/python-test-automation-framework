import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def driver():
    # headless driver options
    options = Options()
    options.add_argument("--headless") # comment out to see browser

    # set up webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_website_title(driver):

