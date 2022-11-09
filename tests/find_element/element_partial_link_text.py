from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class FindByLinkText():
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def test(self):
        element_by_link_text = self.driver.find_element(By.LINK_TEXT, "SUPPORT")
        if element_by_link_text is not None:
            print("The specified item was found by link text.")

        element_by_partial_link_text = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOME")
        if element_by_partial_link_text is not None:
            print("The specified item was found by partial link text.")
        self.driver.close()


test_find_by_link_text_partial_link_text = FindByLinkText()
test_find_by_link_text_partial_link_text.test()


