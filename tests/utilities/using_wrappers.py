import time

from selenium import webdriver
from tests.utilities.helpers import Helpers
from paths import Paths


class UsingHelpers:

    def test(self):
        page = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
        helpers = Helpers(driver)
        driver.get(page)

        element1 = helpers.get_element(locator="//input[@id='name']", locator_type="xpath")
        element1.send_keys("Tekst")
        time.sleep(3)
        element1.clear()
        time.sleep(3)

        driver.close()


run_test_using_helpers = UsingHelpers()
run_test_using_helpers.test()
