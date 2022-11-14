from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class ListOfElements:
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def test(self):
        element_list_by_class_name = self.driver.find_elements_by_class_name("inputs")
        length_class_name = len(element_list_by_class_name)
        if element_list_by_class_name is not None:
            print(f"The number of items in the list by class name is: " + str(length_class_name))

        element_list_by_tag_name = self.driver.find_elements(By.TAG_NAME, "h1")
        length_tag_name = len(element_list_by_tag_name)
        if element_list_by_tag_name is not None:
            print(f"The number of items in the list by tag name is: {length_tag_name}.")
        self.driver.close()


test_find_list_of_elements = ListOfElements()
test_find_list_of_elements.test()
