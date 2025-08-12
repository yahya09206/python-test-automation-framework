import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.get("https://practice.cydeo.com/login")