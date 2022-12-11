import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class XpathDynamic:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/"
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def login_via_dynamic_path(self):
        # open page and login
        sign_in = self.driver.find_element(By.LINK_TEXT, "SIGN IN")
        sign_in.click()
        time.sleep(3)

        email_addres = self.driver.find_element(By.ID, "email")
        email_addres.clear()
        email_addres.send_keys("test@email.com")

        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("abcabc")

        login_button = self.driver.find_element(By.CSS_SELECTOR, ".dynamic-button")
        login_button.click()

        # search course
        click_all_courses = self.driver.find_element(By.LINK_TEXT, "ALL COURSES")
        click_all_courses.click()
        time.sleep(2)

        elements = self.driver.find_elements(By.ID, "search")
        for element in elements:
            if element.get_attribute("name") == "course":
                element.click()
                element.clear()
                element.send_keys("JavaScript")

        click_search_button = self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        click_search_button.click()

        course_selection = self.driver.find_element(By.CLASS_NAME, "img-responsive")
        course_selection.click()

        self.driver.close()


run_test_xpath_dynamic = XpathDynamic()
run_test_xpath_dynamic.login_via_dynamic_path()

