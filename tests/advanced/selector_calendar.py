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

    def test(self):
        self.driver.find_element_by_css_selector(css_selector="[aria-controls='wizard-flight-pwa'] .uitk-tab-text")
        # starting field
        departure_dates = self.driver.find_element_by_id(id_="d1-btn")
        departure_dates.click()
        # day selection
        day_selection = self.driver.find_element_by_xpath(xpath="//tbody/tr[4]/td[6]/button[@type='button']")
        day_selection.click()

        time.sleep(2)
        self.driver.close()

    def test2(self):
        # flight card
        self.driver.find_element_by_css_selector(css_selector="[aria-controls='wizard-flight-pwa'] .uitk-tab-text")
        # starting field
        departure_dates = self.driver.find_element_by_id(id_="d1-btn")
        departure_dates.click()

        calendar = self.driver.find_elements(By.XPATH, "//div[@class='uitk-date-picker-menu-months-container']/div[1]//button[@class='uitk-date-picker-day']")
        for element in calendar:
            if element.get_attribute(name="data-day") == "25":
                element.click()
        time.sleep(2)
        self.driver.close()


run_test_calendar_selector = CalendarSelector()
run_test_calendar_selector.test()
# run_test_calendar_selector.test2()

