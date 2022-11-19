from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class FindByIdName:
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def test(self):
        element_by_id = self.driver.find_element(By.ID, "displayed-text")
        if element_by_id is not None:
            print("The specified item was found by id.")

        element_by_name = self.driver.find_element(By.NAME, "show-hide")
        if element_by_name is not None:
            print("The specified item was found by name.")
        self.driver.close()


test_find_by_id_and_name = FindByIdName()
test_find_by_id_and_name.test()
