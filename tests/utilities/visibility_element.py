from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths
from tests.utilities.helpers import Helpers


class ElementVisiblity:

    def test(self):
        page = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)
        helpers = Helpers(driver)
        driver.get(page)

        element_1 = helpers.present_element(locator="name", locator_type=By.ID)
        print(str(element_1))
        element_2 = helpers.check_elements_present(locator="//input[@id='name']", locator_type=By.XPATH)
        print(str(element_2))


run_test_element_visiblity = ElementVisiblity()
run_test_element_visiblity.test()

