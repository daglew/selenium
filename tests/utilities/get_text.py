from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class GetText:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def get_text_test(self):
        switch_tab_example = self.driver.find_element(By.ID, "opentab")
        text_element = switch_tab_example.text
        print(f"The item text is: {text_element}")

        self.driver.close()


run_test_get_text = GetText()
run_test_get_text.get_text_test()

