from utils.test_base import TestBase

from selenium.webdriver.common.by import By

class IframeTest(TestBase):
    def test_for_iframe(self):
        self.driver.get("https://practice.cydeo.com/iframe")

        iframe_element = self.driver.find_element(By.CSS_SELECTOR, "iframe[title^='Rich Text Area']")
        # switch to iframe element
        self.driver.switch_to.frame(iframe_element)

        # locate p tag inside of iframe
        paragraph_tag = self.driver.find_element(By.TAG_NAME, "p")
        expected_text = "Your content goes here."
        actual_text = paragraph_tag.text
        print(paragraph_tag.text)

        # assert p tag is the same
        assert expected_text in actual_text