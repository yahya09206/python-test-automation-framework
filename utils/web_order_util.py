from selenium import webdriver

class WebOrderUtil:


    @staticmethod
    def open_web_order_app(driver):
        """Open the WebOrder application"""
        driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
