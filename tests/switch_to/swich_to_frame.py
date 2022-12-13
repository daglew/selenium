import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class SwitchToFrame:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.execute_script("window.scrollBy(0, 1000);")

    def test_switch_to_frame(self):
        self.driver.switch_to.frame("courses-iframe")
        time.sleep(2)

        elements = self.driver.find_elements(By.ID, "search")
        for element in elements:
            if element.get_attribute("name") == "course":
                element.send_keys("python")

        time.sleep(2)

        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        self.driver.find_element(By.ID, "name").send_keys("Test Successful")

        time.sleep(2)
        self.driver.close()


run_switch_to_frame = SwitchToFrame()
run_switch_to_frame.test_switch_to_frame()

