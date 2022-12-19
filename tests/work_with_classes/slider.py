import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from paths import Paths


class MoveSlider:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://jqueryui.com/slider/"
        self.driver.get(self.page)

    def test_move_slider(self):
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.XPATH, "//div[@id='slider']/span")
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Element moved successfully.")
            time.sleep(3)
        except:
            print("Element not successfully moved.")
        time.sleep(5)
        self.driver.close()


run_move_slider = MoveSlider()
run_move_slider.test_move_slider()

