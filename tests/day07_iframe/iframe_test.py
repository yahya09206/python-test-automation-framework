from utils.test_base import TestBase


class IframTest(TestBase):
    def test_for_iframe(self):
        self.driver.get("https://practice.cydeo.com/iframe")