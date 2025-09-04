from utils.test_base import TestBase

from selenium.webdriver.common.by import By


class ExplicitWaitTest(TestBase):
    def test_for_explicit_wait(self):
        self.driver.get("practice.cydeo.com/dynamic_controls")

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Example 7").click()
