from utils.test_base import TestBase

from selenium.webdriver.common.by import By


class WebOrderTest(TestBase):
    def test_web_order(self):
        self.driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")

        self.driver.find_element(By.ID, "ctl00_MainContent_username").send_keys("Tester")