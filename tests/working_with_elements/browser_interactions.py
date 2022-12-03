from selenium import webdriver
from paths import Paths


class BrowserInteractions:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        # maximize window
        self.driver.maximize_window()
        # open url
        self.page = "https://courses.letskodeit.com/practice"
        self.driver.get(self.page)
        self.driver.implicitly_wait(15)

    def features_on_the_page(self):
        # get title
        title = self.driver.title
        print("Current page title is: " + title)
        # get current url
        current_url = self.driver.current_url
        print("Current url of thr web pags is: " + current_url)
        # browser refresh
        self.driver.refresh()
        print("Browser refreshed 1st time.")
        self.driver.get(self.driver.current_url)
        print("Browser refreshed 2nd time")
        # open another page
        self.driver.get("https://courses.letskodeit.com/login")
        # step back
        self.driver.back()
        print("Go on step back in browser history.")
        # step forward
        self.driver.forward()
        print("Go on step forward in browser history.")
        # get page source
        page_source = self.driver.page_source
        print("Page source: " + page_source)
        # close browser/ quit browser
        # driver.quit()
        self.driver.close()


test_page = BrowserInteractions()
test_page.features_on_the_page()

