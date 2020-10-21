import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.About_us import About_us

baseurl = "https://www.slcmanagement.com/inv/About+us?vgnLocale=en_CA"


# client sign in
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
def about_us(driver):
    obj = About_us(driver)
    yield obj


@pytest.mark.usefixtures("driver", "about_us")
class Tests():
    def test_23_verify_url8_title(self, about_us):
        time.sleep(3)
        about_us.verify_title()

    def test_24_validate_Footer_links(self, driver, about_us):
        about_us.verify_footer_quicklinks("footer_links", breadcrumb_status=True)

    def test_25_verify_disclosure_text(self, driver, about_us):
        about_us.verify_disclosure()

    def test_26_verify_breadcrumb(self, about_us):
        about_us.verify_breadcrumb()

    def test_27_verify_page_header_text(self, about_us):
        about_us.verify_page_header_text()

    def test_28_verify_CAD_tab(self, about_us):
        about_us.verify_CAD_tab()

    def test_29_verify_USD_tab(self, about_us):
        about_us.verify_USD_tab()

    def test_30_verify_moving_to_join_us_page(self, about_us):
        about_us.job_postings()

    # def test_47_verify_header(self, about_us):
    #     time.sleep(1)
    #     about_us.verify_header()
    #
    # def test_48_verify_breadcrumb(self, about_us):
    #     about_us.verify_active_breadcrumb()
    #
    # def test_49_verify_who_we_are_page_opens_on_clicking_btn(self, about_us):
    #     about_us.move_to_who_we_are_page()
    #
    # def test_50_verify_Investment_management_page_opens_on_clicking_btn(self, about_us):
    #     about_us.move_to_Investment_management_page()
    #
    # def test_51_verify_sponsorship_page_opens_on_clicking_btn(self, about_us):
    #     about_us.move_to_sponsorship_page()


if __name__ == '__main__':
    pytest.main()
