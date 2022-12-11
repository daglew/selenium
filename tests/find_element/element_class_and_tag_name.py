import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class FindByClassTagName:
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def searching_by_tag_name(self):
        element_by_class_name = self.driver.find_element(By.CLASS_NAME, "inputs")
        if element_by_class_name is not None:
            print("The specified item was found by class name.")
            element_by_class_name.send_keys("Testing")

        element_by_tag_name = self.driver.find_element(By.TAG_NAME, "a")
        if element_by_tag_name is not None:
            print("The specified item was found by tag name:" + element_by_tag_name.text)

        time.sleep(10)
        self.driver.close()


test_find_by_class_name_and_tag_name = FindByClassTagName()
test_find_by_class_name_and_tag_name.searching_by_tag_name()
