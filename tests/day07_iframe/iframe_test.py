from tests.day05_css_xpath_pytest.test_title import driver
from utils.test_base import TestBase

from selenium.webdriver.common.by import By

class IframTest(TestBase):
    def test_for_iframe(self):
        self.driver.get("https://practice.cydeo.com/iframe")

        iframe_element = self.driver.find_element(By.CSS_SELECTOR, "iframe[title^='Rich Text Area']")
        # switch to iframe element
        self.driver.switch_to.frame(iframe_element)