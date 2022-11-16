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

    def test(self):
        list_elements_radio_button = self.driver.find_elements(By.XPATH, "")





run_test_list_elements = ListElementsWorking
run_test_list_elements.test()