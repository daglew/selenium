from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class FindByXpathCss():
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def test(self):
        element_by_id = self.driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if element_by_id is not None:
            print("The specified item was found by xpath.")

        element_by_name = self.driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if element_by_name is not None:
            print("The specified item was found by css selector.")
        self.driver.close()


test_find_by_id_and_name = FindByXpathCss()
test_find_by_id_and_name.test()


