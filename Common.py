import time
from urllib.parse import urljoin, urlparse

import pytest
import requests
from lxml import html

homeurl = "https://www.slcmanagement.com/inv/"


class Common():
    def __init__(self, driver):
        self.driver = driver

    common_locators = {
        "search_btn": "//a[contains(text(),'Search')]",
        "input_searchbox": "//input[@id='q']",
        "search_suggestions": "//div[@class='search-autocomplete']",
        "search_submit": "//div[@class='button-wrapper']//input",
        "footer_links": "//*[@class='footer-links']//a",
        "active_breadcrumb": "//ol[@class='breadcrumb']//li[@class='active']",
        "disclosure": "//div[@id='disc-aggrement']//p",
        "footer_section_3": "//*[@class='row global-footer-section3']",
        "page_header": "//h1[1]"

    }

    def is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def verify_search(self):
        self.driver.find_element_by_xpath(self.common_locators["search_btn"]).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.common_locators["input_searchbox"]).send_keys("investment")
        time.sleep(4)
        search_text = self.driver.find_element_by_xpath(self.common_locators["search_suggestions"]).text
        # self.driver.find_element_by_xpath(self.locators["input_searchbox"]).submit()
        self.driver.find_element_by_xpath(self.common_locators["search_submit"]).click()
        time.sleep(3)
        newtitle = self.driver.title
        print(newtitle)
        assert search_text
        print(search_text)

    def verify_footer_quicklinks(self, footer_xpath, breadcrumb_status=False):
        footer_links = self.driver.find_elements_by_xpath(self.common_locators[footer_xpath])
        # for link in footer_links:
        #     print(link.text)
        count = 0
        for link in footer_links:
            if link.text != "Sign in":
                try:
                    url = link.get_attribute('href')
                    print(url)
                    if not self.is_valid(link.get_attribute('href')):
                        url = urljoin(homeurl, link.get_attribute('href'))
                    page = requests.get(url)
                    print(page.status_code)
                    content = html.fromstring(page.content)
                    title = content.findtext('.//title')
                    breadcrumb = content.xpath(self.common_locators["active_breadcrumb"] + "/span/text()")
                    if breadcrumb_status == True:
                        assert breadcrumb
                        assert title
                        print("#", count)
                        print("LINK TEXT:", link.text)
                        print("TITLE:", title)
                        print("BREADCRUMB:", breadcrumb[0])
                    print("LINK TEXT:", link.text)
                    print()
                except Exception as err:
                    print("#", count)
                    print("error occurred", link.text, err)
                    pytest.fail("FAILED, something wrong with footer links", pytrace=False)
            count = count + 1

    def verify_disclosure(self):
        disclosure_element_list = self.driver.find_elements_by_xpath(self.common_locators["disclosure"])

        print(len(disclosure_element_list))

        if len(disclosure_element_list) == 10:
            print("PASSED length test")

        for i in disclosure_element_list:
            print(i.text)
            assert i.text

        # print(disclosure_text.text)
        # assert disclosure_text

    def verify_breadcrumb(self):
        assert self.driver.find_element_by_xpath(self.common_locators["active_breadcrumb"])

    def verify_page_header_text(self):
        header = self.driver.find_element_by_xpath(self.common_locators["page_header"]).text
        print(header)
        assert header

