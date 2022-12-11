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

    def test_automatic_hint(self):
        time.sleep(3)
        air_ticket = self.driver.find_element(By.XPATH, "//span[@title='Bilety lotnicze']")
        air_ticket.click()
        time.sleep(3)

        target_place = "Honolulu, Stany Zjednoczone - Lotnisko Honolulu [HNL]"

        field_to_enter = self.driver.find_element(By.ID, "MultisearchesTo1")
        field_to_enter.click()
        field_to_enter.send_keys("Hon")

        hint_frame = self.driver.find_element(By.ID, "autocomplete_results")
        inner_html = hint_frame.get_attribute("innerHTML")
        # print(inner_html)

        list_elements = hint_frame.find_elements(By.TAG_NAME, "li")
        time.sleep(3)

        for element in list_elements:
            if target_place in element.text:
                element.click()
                break

        time.sleep(2)
        self.driver.close()


run_automatic_filing = AutomaticFiling()
run_automatic_filing.test_automatic_hint()

