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
        # self.driver.switch_to.frame(frame_reference="courses-iframe")
        self.driver.switch_to.frame(frame_reference="zen_all_courses_dynamic")
        # self.driver.switch_to.frame(frame_reference="courses-iframe")
        time.sleep(2)

        searhc_box = self.driver.find_element(By.ID, "search")
        searhc_box.send_keys("python")
        time.sleep(2)

        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        self.driver.find_element(By.ID, "name").send_keys("Test Successful")

        time.sleep(2)
        self.driver.close()


run_switch_to_frame = SwitchToFrame()
run_switch_to_frame.test_switch_to_frame()

