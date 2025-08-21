from day02_locators.get_element_attribute import driver
from utils.test_base import TestBase


class YahooSearchTest(TestBase):
    def test_yahoo_search_home_page(self):
        self.driver.get("https://search.yahoo.com")
        expected_title = "Yahoo Search - Web Search"
        assert expected_title == driver.title, f"Expected '{expected_title}' but got '{driver.title}'"
