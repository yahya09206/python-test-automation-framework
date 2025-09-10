import unittest
import time


from utils.test_base import TestBase
from selenium.webdriver.common.by import By
from web_order_util import WebOrderUtil


class WebOrderTest(TestBase, WebOrderUtil):
    def test_web_order(self):
        self.driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")

        web_or

        self.driver.find_element(By.ID, "ctl00_MainContent_username").send_keys("Tester")
        self.driver.find_element(By.ID, "ctl00_MainContent_password").send_keys("test")
        self.driver.find_element(By.ID, "ctl00_MainContent_login_button").click()

        time.sleep(3)