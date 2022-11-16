import time
from selenium import webdriver
from paths import Paths


class CheckBoxesAndRadioButtons:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def test_checkbox_and_radio_button(self):
        bmw_radio_button = self.driver.find_element_by_id("bmwradio")
        bmw_radio_button.click()

        time.sleep(4)
        beznz_radio_button = self.driver.find_element_by_id("benzradio")
        beznz_radio_button.click()

        time.sleep(4)
        honda_radio_button = self.driver.find_element_by_id("hondaradio")
        honda_radio_button.click()

        bmw_checkbox = self.driver.find_element_by_id("bmwcheck")
        bmw_checkbox.click()

        time.sleep(4)
        beznz_checkbox = self.driver.find_element_by_id("benzcheck")
        beznz_checkbox.click()

        time.sleep(4)
        honda_checkbox = self.driver.find_element_by_id("hondacheck")
        honda_checkbox.click()

        print("Is the radio button selected?" + str(bmw_radio_button.is_selected()))
        print("Is the radio button selected?" + str(beznz_radio_button.is_selected()))
        print("Is the radio button selected?" + str(honda_radio_button.is_selected()))
        print("Is the checkbox selected?" + str(bmw_checkbox.is_selected()))
        print("Is the checkbox selected?" + str(beznz_checkbox.is_selected()))
        print("Is the checkbox selected?" + str(honda_checkbox.is_selected()))

        self.driver.close()


run_test_checkboxs_radiobuttons = CheckBoxesAndRadioButtons()
run_test_checkboxs_radiobuttons.test_checkbox_and_radio_button()