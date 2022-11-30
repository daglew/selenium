from selenium import  webdriver

from paths import Paths
from tests.wait_types.wait_type import WaitType
import time


class ExplicitWait2:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        self.driver.implicitly_wait(15)
        self.driver.get(self.page)

    def test(self):
        wait = WaitType(self.driver)
        element = wait.for_element_wait(locator="//a[@href='/sign_in']", type_locator="xpath")
        element.click()

        time.sleep(5)
        self.driver.close()


run_test_explicit_wait2= ExplicitWait2()
run_test_explicit_wait2.test()

