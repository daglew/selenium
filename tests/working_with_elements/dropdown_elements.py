import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from paths import Paths


class DropdownElements:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def test(self):
        element = self.driver.find_element_by_id("carselect")
        choose = Select(element)

        choose.select_by_value("bmw")
        print(f"Choose Bmw by value.")
        time.sleep(2)

        choose.select_by_index(1)
        print(f"Choose benz by index.")
        time.sleep(2)

        choose.select_by_visible_text("Honda")
        print(f"Choose honda by visible tekst.")
        time.sleep(2)

        choose.select_by_value("bmw")
        print(f"Choose Bmw by value.")
        time.sleep(2)

        self.driver.close()


run_test_dropdown_elements = DropdownElements()
run_test_dropdown_elements.test()
