import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class SwitchToWindow:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(5)

# main window -> parent handle
# click open window button
# search for all handles (there should be two handles)
# switch to window and search course
# switch back to the parent handle

    def test_switch_to_window(self):
        self.driver.find_element(By.ID, "openwindow").click()
        main_window = self.driver.current_window_handle
        print(f"Parent Handle: {main_window}")
        windows = self.driver.window_handles

        for window in windows:
            print(f"Handle: {window}")
            if window != main_window:
                self.driver.switch_to.window(window)
                print(f"Switched to window: {window}")
                elements = self.driver.find_elements(By.ID, "search")
                for element in elements:
                    if element.get_attribute("name") == "course":
                        element.send_keys("python")
                time.sleep(2)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        self.driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(2)
        self.driver.close()


run_switch_to_window = SwitchToWindow()
run_switch_to_window.test_switch_to_window()

