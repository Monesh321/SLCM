import time
from urllib.parse import urlparse

from Pages.Common import Common

homeurl = "https://www.slcmanagement.com/inv"


class About_us(Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "CAD_tab": "//span[contains(text(),'CAD')]",
        "USD_tab": "//span[contains(text(),'USD')]",
        "CAD_currency": "//sub[contains(text(),'CAD')]",
        "USD_currency": "//sub[contains(text(),'USD')]",
        "view_jobs_btn": "//a[contains(text(),'View our current job postings')]"
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

    def verify_CAD_tab(self):
        self.driver.find_element_by_xpath(self.locators["CAD_tab"]).click()
        time.sleep(1)
        currency = self.driver.find_element_by_xpath(self.locators["CAD_currency"]).text
        print(currency)
        assert currency == "CAD"

    def verify_USD_tab(self):
        self.driver.find_element_by_xpath(self.locators["USD_tab"]).click()
        time.sleep(1)
        currency = self.driver.find_element_by_xpath(self.locators["USD_currency"]).text
        print(currency)
        assert currency == "USD"

    def job_postings(self):
        currenturl = self.driver.current_url
        print("CURRENT URL:", currenturl)
        self.driver.find_element_by_xpath(self.locators["view_jobs_btn"]).click()
        time.sleep(1)
        newurl = self.driver.current_url
        print("NEW URL:", newurl)

        assert currenturl != newurl
