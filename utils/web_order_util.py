
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebOrderUtil:


    @staticmethod
    def open_web_order_app(driver):
        """Open the WebOrder application"""
        driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")

    @staticmethod
    def login(driver):
        driver.findElement(By.ID, "ctl00_MainContent_username").sendKeys("Tester")
        driver.findElement(By.ID, "ctl00_MainContent_password").sendKeys("test")
        driver.findElement(By.ID, "ctl00_MainContent_login_button").click()

