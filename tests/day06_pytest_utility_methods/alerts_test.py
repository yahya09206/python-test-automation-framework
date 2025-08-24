import time

from utils.test_base import TestBase
from selenium.webdriver.common.by import By

class AlertsTest(TestBase):
    def test_for_alerts(self):

        self.driver.get("https://practice.cydeo.com/javascript_alerts")

        self.driver.find_element(By.XPATH, "//button[.='Click for JS Alert']").click()

        time.sleep(2)
        print(self.driver.switch_to.alert.text)
        time.sleep(2)


