from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from tests.utilities.helpers import Helpers


class WaitType:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)

    def for_element_wait(self, locator, type_locator="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type_element = self.helpers.get_element_type(locator_type=type_locator)

            print(f"Waiting for a maximum of: {str(timeout)} seconds for element to be visible.")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type_element, locator)))
            print(f"Element appeared on the page.")
        except:
            print(f"Element not appeared on the page.")
        return element

