from selenium.webdriver import ActionChains

from utils.test_base import TestBase

from selenium.webdriver.common.by import By


class ActionsClassTest(TestBase):
    def test_for_actions_class(self):
        image_element_one = self.driver.find_element(By.XPATH, "//div[@class='figure']/img[1]")

        # create instance of Actions class by passing driver object
        actions = ActionChains(self.driver)
        actions.move_to_element(image_element_one).perform()

        first_profile_element = self.driver.find_element(By.XPATH, "//h5[.='name: user1']")
        assert first_profile_element.is_displayed()