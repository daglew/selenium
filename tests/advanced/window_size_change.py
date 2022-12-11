import time
from selenium import webdriver
from paths import Paths


class WindowSizeChange:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        # self.driver.maximize_window()
        self.driver.get("https://courses.letskodeit.com/practice")
        self.driver.implicitly_wait(5)

    def window_size(self):
        height = self.driver.execute_script("return window.innerHeight;")
        width = self.driver.execute_script("return window.innerWidth;")
        print(f"Height: {str(height)}.")
        print(f"Width: {str(width)}.")

        time.sleep(10)
        self.driver.close()


run_window_size_change = WindowSizeChange()
run_window_size_change.window_size()

