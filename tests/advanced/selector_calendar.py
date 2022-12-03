import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class CalendarSelector:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://www.expedia.com/"
        self.driver.implicitly_wait(5)
        self.driver.get(self.page)

    def day_selection_by_specifying_xpath(self):
        # click calendar check-in
        departure_dates = self.driver.find_element(By.ID, "d1-btn")
        departure_dates.click()
        # selection day
        day_selection = self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[6]/button[@type='button']")
        day_selection.click()

        time.sleep(2)
        self.driver.close()

    def day_selection_with_condition(self):
        # click calendar check-in
        departure_dates = self.driver.find_element(By.ID, "d1-btn")
        departure_dates.click()
        # selection day
        day_selection = self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[6]/button[@type='button']")
        day_selection.click()

        calendar = self.driver.find_elements(By.XPATH, "//div[@class='uitk-date-picker-menu-months-container']/div[1]//button[@class='uitk-date-picker-day']")
        for element in calendar:
            if element.get_attribute(name="data-day") == "25":
                element.click()
        time.sleep(2)
        self.driver.close()


run_test_calendar_selector = CalendarSelector()
# run_test_calendar_selector.day_selection_by_specifying_xpath()
run_test_calendar_selector.day_selection_with_condition()

