from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class FindElement:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://www.google.com"
        self.driver.get(self.page)
        self.driver.implicitly_wait(4)

    def element_find(self):
        self.driver.find_element(By.ID, "W0wltc").click()
        first_element = self.driver.find_element_by_xpath("//input[@role='combobox']")
        on_first_element = first_element.is_enabled()
        print("on first element is enabled :" + str(on_first_element))

        first_element2 = self.driver.find_element_by_xpath("//div[@class='a4bIc']")
        on_first_element2 = first_element2.is_enabled()
        print("on first element is enabled :" + str(on_first_element2))

        first_element3 = self.driver.find_element_by_xpath("//div[@class='SDkEP']")
        on_first_element3 = first_element3.is_enabled()
        print("on first element is enabled :" + str(on_first_element3))

        first_element.send_keys("dog")

        self.driver.close()


run = FindElement()
run.element_find()

