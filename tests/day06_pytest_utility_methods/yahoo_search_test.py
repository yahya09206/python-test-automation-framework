from day02_locators.get_element_attribute import driver
from utils.test_base import TestBase


class YahooSearchTest(TestBase):
    def test_yahoo_search_home_page(self):
        print("Initial URL:", self.driver.current_url)
        self.driver.get("https://search.yahoo.com")
        print("After navigation URL:", self.driver.current_url)
        expected_title = "Yahoo Search - Web Search"
        actual_title = self.driver.title
        assert expected_title in actual_title, f"{expected_title} in title but got {actual_title}"

    def test_yahoo_search_results_page(self):
        self.driver.get("https://search.yahoo.com")