import os
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestBase(unittest.TestCase):
    """Setup WebDriver before each test."""
    browser = os.getenv("BROWSER", "chrome").lower() # default will = chrome

