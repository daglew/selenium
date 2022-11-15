from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class ChecksBoxAndRadioButtons:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def test_checkboks_and_radio_button(self):
        bmw_radio_button =