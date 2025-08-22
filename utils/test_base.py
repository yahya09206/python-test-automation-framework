import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class TestBase(unittest.TestCase):

    def setUp(self):
        """Setup WebDriver before each test."""
        browser = os.getenv("BROWSER", "chrome").lower() # default will = chrome

        if browser == "chrome":
            chrome_options = ChromeOptions()
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options,
            )
            #self.driver.implicitly_wait(10)
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless=new")
            self.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=firefox_options
            )
        else:
            raise ValueError(f"Unsupported browser: (browser)")


    def tearDown(self):
        if self.driver:
            self.driver.quit()


