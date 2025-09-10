import os
import unittest
from datetime import time

from selenium.webdriver.common.by import By

from utils.test_base import TestBase


class WebOrderTest(TestBase):
    def test_web_order(self):
        self.driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")

        web

        self.driver.find_element(By.ID, "ctl00_MainContent_username").send_keys("Tester")
        self.driver.find_element(By.ID, "ctl00_MainContent_password").send_keys("test")
        self.driver.find_element(By.ID, "ctl00_MainContent_login_button").click()

        time.sleep(3)