from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

from webdriver_manager.chrome import ChromeDriverManager


class Driver:

    _driver = None

    @classmethod
    def get_driver(cls):
        browser_name = os.getenv("BROWSER", "chrome").lower()

        if cls._driver is None:
            if browser_name == "chrome":
                cls._driver = webdriver.Chrome(
                    service=ChromeService()
                )