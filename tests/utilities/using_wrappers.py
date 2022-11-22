import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utilities.helpers import Helpers
from paths import Paths


class UsingHelpers:

    def test(self):
        page = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
        he = Helpers(driver)
        driver.get(page)

        find_item_1 = he.enter_by_type("name")
        find_item_1.send_keys("Test")
        time.sleep(3)
        find_item_2 = he.by_element("//input[@id='name']|", locator_type="xpath")
        find_item_2.clear()
        driver.close()


run_test_using_helpers = UsingHelpers()
run_test_using_helpers.test()
