from utils.test_base import TestBase


class WebOrderTest(TestBase):
    def test_web_order(self):
        self.driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")