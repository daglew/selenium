import time

from selenium import webdriver
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
        self.driver.find_element_by_class_name(name="#location-field-leg1-origin-menu .uitk-form-field-trigger")






        time.sleep(5)
        self.driver.close()


run_test_calendar_selector = CalendarSelector()
run_test_calendar_selector.test()

