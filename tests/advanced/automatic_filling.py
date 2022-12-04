from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from paths import Paths


class AutomaticFiling:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://www.lotnisko-chopina.pl/"
        self.driver.implicitly_wait(2)
        self.driver.get(self.page)

    def automatic_hint(self):
        air_ticket = self.driver.find_element(By.XPATH, "//span[@title='Bilety lotnicze']")
        air_ticket.click()

        field_to_enter = self.driver.find_element(By.ID, "field to enter")
        field_to_enter.click()
        field_to_enter.send_keys("Hon")

        target_place = "Honolulu, Stany Zjednoczone - Lotnisko Honolulu [HNL]"

