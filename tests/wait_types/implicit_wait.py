import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class ImplicitWait:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        self.driver.implicitly_wait(15)
        self.driver.get(self.page)

    def test(self):
        sign_in = self.driver.find_element(By.LINK_TEXT, "Login")
        sign_in.click()
        time.sleep(3)

        email_addres = self.driver.find_element(By.ID, "email")
        email_addres.clear()
        email_addres.send_keys("test@email.com")

        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("abcabc")

        log_in_button = self.driver.find_element(By.NAME, "commit")
        log_in_button.click()


run_test_implicit_wait = ImplicitWait()
run_test_implicit_wait.test()

