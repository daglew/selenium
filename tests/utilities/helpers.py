from selenium.webdriver.common.by import By


class Helpers:
    def __init__(self, driver):
        self.driver = driver

    def get_element_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print(f"The given locator is invalid: {locator_type}.")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("The specified item was found.")
        except:
            print("The specified item was not found.")
        return element

    def present_element(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("The specified item was found.")
                return True
            else:
                return False
        except:
            print("The specified item was not found.")
            return False

    def check_elements_present(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            list_elements = self.driver.find_elements(by_type, locator)
            if len(list_elements) > 0:
                print("The specified item was found.")
                return True
            else:
                print("The specified item was not found.")
                return False
        except:
            print("The specified item was not found.")
            return False

