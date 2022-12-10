import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class ScrollPage:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.driver.get("https://courses.letskodeit.com/practice")
        self.driver.implicitly_wait(5)

    def scrol_page(self):
        # scroll down
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(3)

        # scroll up
        self.driver.execute_script("window.scrollBy(0, -800);")
        time.sleep(3)

        # scroll page to element
        mouse_hover_element = self.driver.find_element(By.ID, "mousehover")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_element)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, -200);")

        # failed way to scroll item to view
        self.driver.execute_script("window.scrollBy(0,-1000);")
        location = mouse_hover_element.location_once_scrolled_into_view
        print(f"Location: {str(location)}")

        time.sleep(10)
        self.driver.close()


run_scroll_page = ScrollPage()
run_scroll_page.scrol_page()

