import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.People import People

baseurl = "https://www.slcmanagement.com/inv/People/Leadership?vgnLocale=en_CA"


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
def PP_page(driver):
    obj = People(driver)
    yield obj


@pytest.mark.usefixtures("driver", "PP_page")
class Tests():

    def test_10_verify_url2_titles(self, driver, PP_page):
        PP_page.verify_title()

    def test_11_verify_clicking_on_each_leadership_tab_works(self, driver, PP_page):
        PP_page.click_on_each_leadership_tab()


    def test_12_validate_Footer_links(self, driver, PP_page):
        PP_page.verify_footer_quicklinks("footer_links", breadcrumb_status=True)

    def test_13_verify_disclosure_text(self, driver, PP_page):
        PP_page.verify_disclosure()

    def test_14_verify_breadcrumb(self, PP_page):
        PP_page.verify_breadcrumb()

    def test_15_verify_page_header_text(self, PP_page):
        PP_page.verify_page_header_text()