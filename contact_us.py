import time
from urllib.parse import urlparse
from selenium.webdriver.support.ui import Select

import requests

# from requests_html import HTML
from Pages.Common import Common


class contact_us(Common):
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
        "phone": "//p[contains(text(),'Phone: 1-877-344-1434')]",
        "name": "//input[@id='control_Name']",
        "email": "//input[@id='control_EMAIL']",
        "region": "//select[@id='control_Region']",
        "organization": "//select[@id='control_Organization']",
        "message": "//textarea[@id='control_message']",
        "submit": "//button[@id='contactformSubmit']",
        "success_message": "//div[@id='success_message']"
    }

    def verify_phone_displayed(self):
        phone = self.driver.find_element_by_xpath(self.locators["phone"]).text
        assert phone

    def fill_and_submit_contact_us_form(self):
        self.driver.find_element_by_xpath(self.locators["name"]).send_keys("Monish Ali")
        self.driver.find_element_by_xpath(self.locators["email"]).send_keys("mrksshali@gmail.com")

        select = Select(self.driver.find_element_by_xpath(self.locators["region"]))

        # select by visible text
        select.select_by_visible_text('Canada')
        # alloptions = select.options
        # print(len(alloptions))
        # for option in alloptions:
        #     print(option.text)

        # select by value
        # select.select_by_value('1')
        select = Select(self.driver.find_element_by_xpath(self.locators["organization"]))
        select.select_by_index(2)
        #
        # alloptions = select.options
        #
        # print(len(alloptions))
        #
        # for option in alloptions:
        #     print(option.text)

        self.driver.find_element_by_xpath(self.locators["message"]).send_keys("testing")
        self.driver.find_element_by_xpath(self.locators["submit"]).click()
        time.sleep(3)
        success_msg = self.driver.find_element_by_xpath(self.locators["success_message"]).text
        print(success_msg)
        assert success_msg != ""
