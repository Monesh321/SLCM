import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.contact_us import contact_us

baseurl = "https://www.slcmanagement.com/inv/Contact+us?vgnLocale=en_CA"


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
def contact(driver):
    obj = contact_us(driver)
    yield obj


@pytest.mark.usefixtures("driver", "contact")
class Tests():
    def test_31_verify_url7_title(self, contact):
        time.sleep(3)
        contact.verify_title()

    def test_32_validate_Footer_links(self, driver, contact):
        contact.verify_footer_quicklinks("footer_links", breadcrumb_status=True)

    def test_33_verify_disclosure_text(self, driver, contact):
        contact.verify_disclosure()

    def test_34_verify_breadcrumb(self, contact):
        contact.verify_breadcrumb()

    def test_35_verify_page_header_text(self, contact):
        contact.verify_page_header_text()

    def test_36_verify_phone_displayed(self, contact):
        contact.verify_phone_displayed()

    def test_37_validate_contact_us_form(self, contact):
        contact.fill_and_submit_contact_us_form()

if __name__ == '__main__':
    pytest.main()