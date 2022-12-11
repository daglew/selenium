import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class ScreenshotsGeneric:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        self.driver.implicitly_wait(3)
        self.driver.get(self.page)

    def test_screenshots(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").send_keys("abc@email.com")
        self.driver.find_element(By.ID, "password").send_keys("abc")
        self.driver.find_element(By.NAME, "commit").click()

        path_to_the_dump_folder = "D:\\screenshots tests\\"

        try:
            self.driver.save_screenshot(path_to_the_dump_folder)
            print(f"The screenshot was saved in: {path_to_the_dump_folder}.")
        except NotADirectoryError:
            print("Has not been saved, it is a problem with the catalog.")

    # takes screenshots of the currently open web page.
    def screenshots_generic_test(self):
        name_file = str(round(time.time() * 1000)) + ".png"
        folder_path = "D:\\screenshots tests\\"
        destination_file = folder_path + name_file

        try:
            self.driver.save_screenshot(destination_file)
            print(f"The screenshot was saved in: {destination_file}.")
        except NotADirectoryError:
            print("Has not been saved, it is a problem with the catalog.")

        time.sleep(5)
        self.driver.close()


run_screenshots_generic_test = ScreenshotsGeneric()
run_screenshots_generic_test.screenshots_generic_test()

