import time
from urllib.parse import urljoin
from selenium import webdriver
import requests
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.Common import Common

baseurl = "https://www.slcmanagement.com/inv/People/Leadership?vgnLocale=en_CA"


class People(Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "Executive_leadership": "//a[@id='executiveleadership']",
        "investment_leadership": "//a[@id='investmentsleadership']",
        "business_development": "//a[@id='businessdevelopment']"

    }

    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def click_on_each_leadership_tab(self):
        self.driver.find_element_by_xpath(self.locators["Executive_leadership"]).click()
        self.driver.find_element_by_xpath(self.locators["investment_leadership"]).click()
        self.driver.find_element_by_xpath(self.locators["business_development"]).click()


    # def get_all_data_from_a_table(self, table_id):
    #
    #     table = self.driver.find_element(By.ID, table_id)
    #     rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
    #     for row in rows:
    #         # Get the columns (all the column 2)
    #         cols = [col.text for col in row.find_elements(By.TAG_NAME, "td")]  # note: index start from 0, 1 is col 2
    #         if cols != []:
    #             print(cols)  # prints text from the element
    #
