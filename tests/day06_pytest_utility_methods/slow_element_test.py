from selenium import webdriver

from utils.test_base import TestBase
from selenium.webdriver.common.by import By

class SlowElementTest(TestBase):
    def test_slow_element(self):
        self.driver.get("https://practice.cydeo.com/dynamic_controls")
        self.driver.find_element(By.XPATH, "//button[.='Remove']").click()

        its_gone = self.driver.find_element(By.ID, "message")
        print(its_gone.text)