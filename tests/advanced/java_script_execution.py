import time

from selenium import webdriver
from paths import Paths


class JavaScript:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        # self.page = "https://courses.letskodeit.com/practice"
        # self.driver.get(self.page)
        self.driver.execute_script("window.location = 'https://courses.letskodeit.com/practice';")
        self.driver.implicitly_wait(5)

    def test_java_script_execute(self):
        input_your_name = self.driver.execute_script("return document.getElementById('name');")
        input_your_name.send_keys("Test.")
        time.sleep(5)
        self.driver.close()


run_test_java_script = JavaScript()
run_test_java_script.test_java_script_execute()

