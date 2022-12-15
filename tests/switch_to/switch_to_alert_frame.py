import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class SwitchToAlertFrame:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)

    def test_switch_to(self):
        self.driver.find_element(By.ID, "name").send_keys("Dagmara")
        self.driver.find_element(By.ID, "alertbtn").click()
        time.sleep(3)
        first_way_alarm = self.driver.switch_to.alert
        first_way_alarm.accept()
        time.sleep(3)
        self.driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(3)
        alarm_second_way = self.driver.switch_to.alert
        alarm_second_way.dismiss()
        time.sleep(3)

        self.driver.close()


run_test_swich_to_alert_frame = SwitchToAlertFrame()
run_test_swich_to_alert_frame.test_switch_to()

