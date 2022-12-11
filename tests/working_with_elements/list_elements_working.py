import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class ListElementsWorking:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def selecting_button(self):
        list_elements_radio_button = self.driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name, 'cars')]")
        lenght_list_radio_button = len(list_elements_radio_button)
        print(f"The length of the list is: {lenght_list_radio_button}")

        for radio_button in list_elements_radio_button:
            marked_button = radio_button.is_selected()

            if not marked_button:
                radio_button.click()
                time.sleep(3)

        self.driver.close()


run_test_list_elements = ListElementsWorking()
run_test_list_elements.selecting_button()

