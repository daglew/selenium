from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class FindByXpathCss:
    def __init__(self):
        self.page = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def searching_by_xpath_and_css_selector(self):
        element_by_xpath = self.driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if element_by_xpath is not None:
            print("The specified item was found by xpath.")

        element_by_css_selector = self.driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if element_by_css_selector is not None:
            print("The specified item was found by css selector.")
        self.driver.close()


test_find_by_xpath_and_css_selector = FindByXpathCss()
test_find_by_xpath_and_css_selector.searching_by_xpath_and_css_selector()
