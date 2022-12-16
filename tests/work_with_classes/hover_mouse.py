import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from paths import Paths


class HoverMouse:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)

    def test_hover_mouse(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)
        element_button_mouse_hover = self.driver.find_element(By.ID, "mousehover")
        item_mouse_hover = ".//div[@class='mouse-hover']//a[text()='Top']"

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(to_element=element_button_mouse_hover).perform()
            print("Mouse hover on element.")
            time.sleep(3)
            top_of_page = self.driver.find_element(By.XPATH, item_mouse_hover)
            top_of_page.click()
            print("Item clicked.")
        except:
            print("Mouse hover over item failed.")
        self.driver.close()


run_test_hover_mouse = HoverMouse()
run_test_hover_mouse.test_hover_mouse()

