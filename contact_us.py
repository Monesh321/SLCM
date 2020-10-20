from urllib.parse import urlparse

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
        "submit": "//button[@id='contactformSubmit']"
    }

    def verify_phone_displayed(self):
        phone = self.driver.find_element_by_xpath(self.locators["phone"]).text
        assert phone

    def fill_and_submit_contact_us_form(self):
        self.driver.find_element_by_xpath(self.locators["name"]).send_keys("Monish Ali")
        self.driver.find_element_by_xpath(self.locators["email"]).send_keys("mrksshali@gmail.com")

