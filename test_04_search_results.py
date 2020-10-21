import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.search_results import search_result

baseurl = "https://www.slcmanagement.com/inv/Search/Search+Results?q=investments"


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
def search(driver):
    obj = search_result(driver)
    yield obj


@pytest.mark.usefixtures("driver", "search")
class Tests():
    def test_16_verify_url4_title(self, search):
        time.sleep(3)
        search.verify_title()

    def test_17_verify_search_results_count_is_displayed_correctly(self, search):
        search.verify_result_count_displayed()

    def test_18_verify_search_results_links_are_valid_urls(self, search):
        search.verify_search_result_links()

    def test_19_validate_Footer_links(self, driver, search):
        search.verify_footer_quicklinks("footer_links", breadcrumb_status=True)

    def test_20_verify_disclosure_text(self, driver, search):
        search.verify_disclosure()

    def test_21_verify_breadcrumb(self, search):
        search.verify_breadcrumb()

    def test_22_verify_page_header_text(self, search):
        search.verify_page_header_text()



if __name__ == '__main__':
    pytest.main()