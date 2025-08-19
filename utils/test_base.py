import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class TestBase(unittest.TestCase):

    def setUp(self):
        """Setup WebDriver before each test."""
        browser = os.getenv("BROWSER", "chrome").lower() # default will = chrome

        if browser == "chrome":
            chrome_options = ChromeOptions
            chrome_options.add_argument("--headless=new")
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )


