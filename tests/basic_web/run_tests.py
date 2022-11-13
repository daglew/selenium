from selenium import webdriver

from paths import Paths


class RunTests:
    def test(self):
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        driver.get("https://courses.letskodeit.com")


run = RunTests()
run.test()
