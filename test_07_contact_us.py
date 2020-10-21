import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.contact_us import contact_us

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/Contact+us?vgnLocale=en_CA"


# client sign in
@pytest.fixture(scope='function', autouse=True)
def driver(request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument(f"--window-size={1920},{3926}")
    # chrome_options.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(options=chrome_options)
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
    def test_37_verify_url7_title(self, contact):
        time.sleep(3)
        contact.verify_title()

    def test_38_verify_header(self, contact):
        time.sleep(1)
        contact.verify_header_present()

    def test_39_verify_breadcrumb(self, contact):
        contact.verify_breadcrumb_active()

    def test_40_verify_phone_displayed(self, contact):
        contact.verify_phone_displayed()

    def test_41_verify_fax_displayed(self, contact):
        contact.verify_fax_displayed()

    def test_42_verify_email_displayed(self, contact):
        contact.verify_email_displayed()

    def test_43_verify_Question_1(self, contact):
        contact.verify_Question_1()

    def test_44_verify_Question_2(self, contact):
        contact.verify_Question_2()

    def test_45_verify_Question_3(self, contact):
        contact.verify_Question_3()