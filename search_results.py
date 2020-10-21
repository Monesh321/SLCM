from urllib.parse import urlparse

import pytest
import requests

# from requests_html import HTML
# homeurl = "https://www.sunlifeglobalinvestments.com/Slgi/Search+results?q=investment&action=input"
from Pages.Common import Common


class search_result(Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_valid(self, url):
        """
              Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        status = requests.get(url).status_code
        if bool(parsed.netloc) and bool(parsed.scheme) and status == 200:
            return True
        else:
            print("STATUS:", status)
            print("DOMAIN:", parsed.netloc, "SCHEME:", parsed.scheme)
            return False

    locators = {
        "search_header": "//h1[contains(text(),'Search results')]",
        "breadcrumb_text": "//ol[@class='breadcrumb']//li[@class='active']",
        "result_count": "//span[@id='search-result-num-results']",
        "result_links": "//div[@id='search-result-items']//a",
        "pagination": "//ul[@id='search-result-pagination']//li",
        "previous_enabled": "//li[@class='previous']"
    }
    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def verify_header_present(self):
        header = self.driver.find_element_by_xpath(self.locators["search_header"]).text
        assert "search".casefold() in header.casefold()

    def verify_breadcrumb_active(self):
        breadcrumb = self.driver.find_element_by_xpath(self.locators["breadcrumb_text"]).text
        assert breadcrumb

    def verify_result_count_displayed(self):
        res_count = self.driver.find_element_by_xpath(self.locators["result_count"]).text
        print(res_count)
        assert res_count != True

    def verify_search_result_links(self):
        links = self.driver.find_elements_by_xpath(self.locators["result_links"])
        flag = True
        for link in links:
            url = link.get_attribute("href")
            # print(link.text, ":", url)
            if not self.is_valid(url):
                print(link.text, ":", url, ":Link not valid")
                flag = False
            else:
                print(link.text, ":", url, ":Link Works fine, hence PASSED")

        if flag == False:
            pytest.fail("FAILED", pytrace=False)