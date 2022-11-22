from selenium import webdriver
from selenium.webdriver.common.by import By


class Helpers:
    def __init__(self, driver):
        self.driver = driver

    def enter_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("The locator is invalid.")
        return False

    def by_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.enter_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("The specified item was found.")
        except:
            print("The specified item was not found.")
        return element

