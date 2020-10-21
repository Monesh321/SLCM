import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# baseurl = "https://www.slcmanagement.com/inv?vgnLocale=en_CA"


class Base():
    def __init__(self, baseurl):
        self.baseurl=baseurl


    @pytest.fixture(scope='function', autouse=True)
    def driver(self, request):
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
        driver.get(self.baseurl)

        def driver_teardown():
            print("closing browser")
            driver.close()

        request.addfinalizer(driver_teardown)
        yield driver
