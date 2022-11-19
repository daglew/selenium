from selenium import webdriver
from paths import Paths


class RunTests:
    def test(self):
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com")
        driver.close()


run = RunTests()
run.test()
