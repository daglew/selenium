import time
from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from paths import Paths


class ExplicitWait:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        # self.driver.get(self.page)
        # self.driver.execute_script("window.location = 'https://letskodeit.teachable.com/';")
        # self.driver.find_element(By.XPATH, "//a[text()='Login]").click

    def explicit_wait_test(self):
        self.driver.execute_script("window.location = 'https://letskodeit.teachable.com/';")
        self.driver.find_element(By.XPATH, "//a[@href='/sign_in']").click()

        # Firefox
        # wait = WebDriverWait(self.driver, timeout= 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        #
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='/sign_in]")))
        # element.click()

        time.sleep(5)
        self.driver.close()


run_test_explicit_wait = ExplicitWait()
run_test_explicit_wait.test()

