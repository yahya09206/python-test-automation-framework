import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver()
    # headless driver options
    options = Options()
    options.add_argument("--headless")