from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utils.test_base import TestBase

from selenium.webdriver.common.by import By


class ExplicitWaitTest(TestBase):
    def test_for_explicit_wait(self):
        self.driver.get("https://practice.cydeo.com/dynamic_loading")

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Example 7").click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(visibility_of_element_located(By.XPATH, "//img[@alt='square pants']"))

        print("THE END")
