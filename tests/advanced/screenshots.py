import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class Screenshots:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        self.driver.implicitly_wait(3)
        self.driver.get(self.page)

    def screenshots_test(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").send_keys("abc@email.com")
        self.driver.find_element(By.ID, "password").send_keys("abc")
        self.driver.find_element(By.NAME, "commit").click()

        path_to_the_dump_folder = "D:\\test.png"

        try:
            self.driver.save_screenshot(path_to_the_dump_folder)
            print(f"The screenshot was saved in: {path_to_the_dump_folder}.")
        except NotADirectoryError:
            print("Has not been saved, it is a problem with the catalog.")

        time.sleep(5)
        self.driver.close()


run_screenshots_test = Screenshots()
run_screenshots_test.screenshots_test()

