import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class GetAttribute:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.implicitly_wait(15)
        self.driver.get(self.page)

    def test(self):
        input_enter_your_name = self.driver.find_element(By.ID, "name")
        input_enter_your_name_result = input_enter_your_name.get_attribute("class")

        print(f"Attribute value is: {input_enter_your_name_result}.")
        time.sleep(5)
        self.driver.close()


run_test_get_attribute = GetAttribute()
run_test_get_attribute.test()

