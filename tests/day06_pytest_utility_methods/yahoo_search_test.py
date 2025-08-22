from day02_locators.get_element_attribute import driver
from utils.test_base import TestBase


class YahooSearchTest(TestBase):
    def test_yahoo_search_home_page(self):
        print("Initial URL:", self.driver.current_url)
        self.driver.get("https://search.yahoo.com")
        print("After navigation URL:", self.driver.current_url)
        expected_title = "Yahoos Search - Web Search"
        actual_title = self.driver.title
        assert "Yahoo Search" in actual_title, f"{expected_title} in title but got {actual_title}"
