import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class UsingWrappers:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.implicitly_wait(5)
        self.driver.get(self.page)

    def test(self):

        self.driver.close()


run_test_using_wrappers = UsingWrappers()
run_test_using_wrappers.test()
