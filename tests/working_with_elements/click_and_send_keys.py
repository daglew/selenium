import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class ClickAndSendKeys:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com"
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def test(self):
        login_link = self.driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']/div//a[@href='/login']")
        login_link.click()

        email = self.driver.find_element(By.ID, "email")
        email.send_keys("test")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("test")

        time.sleep(4)

        email.clear()

        time.sleep(4)

        email.send_keys("test")
        self.driver.close()


test_page = ClickAndSendKeys()
test_page.test()

