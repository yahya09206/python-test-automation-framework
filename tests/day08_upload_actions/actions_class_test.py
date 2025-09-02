from utils.test_base import TestBase

from selenium.webdriver.common.by import By


class ActionsClassTest(TestBase):
    def test_for_actions_class(self):
        image_element_one = self.driver.find_element(By.XPATH, "//div[@class='figure']/img[1]")
