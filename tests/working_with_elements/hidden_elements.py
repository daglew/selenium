import time
from selenium import webdriver
from paths import Paths


class HiddenElements:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def test(self):
        box_text_element = self.driver.find_element_by_id("displayed-text")
        box_text_state = box_text_element.is_displayed()

        print(f"Text is vidible? {box_text_state}")
        time.sleep(2)

        self.driver.find_element_by_id("hide-textbox").click()

        box_text_state = box_text_element.is_displayed()

        print(f"Text is vidible? {box_text_state}")

        time.sleep(2)

        self.driver.find_element_by_id("show-textbox").click()

        box_text_state = box_text_element.is_displayed()

        print(f"Text is vidible? {box_text_state}")

        self.driver.close()


run_test_hidden_elements = HiddenElements()
run_test_hidden_elements.test()
