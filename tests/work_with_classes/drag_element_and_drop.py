import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from paths import Paths


class DragElementAndDrop:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://jqueryui.com/droppable/"
        self.driver.get(self.page)

    def test_drag_and_drop(self):
        self.driver.switch_to.frame(0)
        from_small_element = self.driver.find_element(By.ID, "draggable")
        to_large_element = self.driver.find_element(By.ID, "droppable")
        time.sleep(3)
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(from_small_element, to_large_element).perform()
            # actions.click_and_hold(on_element=from_small_element).move_to_element(to_element=to_large_element).release().perform()
            print("Element has been dragged.")
            time.sleep(3)
        except:
            print("Drag and drop failed on element.")
        time.sleep(5)
        self.driver.close()


run_test = DragElementAndDrop()
run_test.test_drag_and_drop()

