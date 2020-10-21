import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.Home import Home
from Tests.Base_Test import Base

baseurl = "https://www.slcmanagement.com/inv?vgnLocale=en_CA"


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument(f"--window-size={1920},{3926}")
    # chrome_options.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(executable_path="/home/monesh/PycharmProjects/SLCM_sunlife/chromedriver",
                              options=chrome_options)
    driver.implicitly_wait(8)
    driver.get(baseurl)

    def driver_teardown():
        print("closing browser")
        driver.close()

    request.addfinalizer(driver_teardown)
    yield driver


@pytest.fixture(scope='function', autouse=True)
def home(driver):
    obj = Home(driver)
    yield obj


@pytest.mark.usefixtures("driver", "home")
class Tests():

    def test_01_verify_page_title(self, driver, home):
        print(driver.title)

    def test_02_verify_signin_btn_is_clickable(self, driver, home):
        home.click_signin_btn()
        home.click_close_btn()

    def test_02_verify_signin_header(self, driver, home):
        home.click_signin_btn()
        # time.sleep(3)
        home.check_signin_header_present()
        home.click_close_btn()

    def test_03_validate_Expertise_mega_menu(self, driver, home):
        home.verify_megamenu_links("Expertise_mega_menu")
        # driver.find_element_by_xpath("").get_attribute()

    def test_04_validate_People_mega_menu(self, driver, home):
        home.verify_megamenu_links("People_mega_menu")

    def test_05_validate_Insights_mega_menu(self, driver, home):
        home.verify_megamenu_links("Insights_mega_menu")

    def test_06_validate_About_us_mega_menu(self, driver, home):
        home.verify_megamenu_links("About_us_mega_menu")

    def test_07_search_functionality(self, driver, home):
        home.verify_search()

    def test_08_validate_Footer_links(self, driver, home):
        home.verify_footer_quicklinks("footer_links", breadcrumb_status=True)

    def test_09_verify_disclosure_text(self, driver, home):
        home.verify_disclosure()


if __name__ == '__main__':
    pytest.main()
