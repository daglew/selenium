from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class FindByIdNsme():
    def test(self):
        page = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(Paths.CHROMEDRIVER_PATH)
        driver.get(page)
        driver.implicitly_wait(15)

        element_by_id = driver.find_element(By.ID, "displayed-text")
        if element_by_id is not None:
            print("Element Found By Id")

