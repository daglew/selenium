from selenium import webdriver

from paths import Paths


class BrowserInteractions:
    def test(self):
        base_url = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        # maximize window
        driver.maximize_window()
        # open url
        driver.get(base_url)
        # get title
        title = driver.title
        print("Current page title is: " + title)
        # get current url
        current_url = driver.current_url
        print("Current url of thr web pags is: " + current_url)
        # browser refresh
        driver.refresh()
        print("Browser refreshed 1st time.")
        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")
        # open another page
        driver.get("https://courses.letskodeit.com/login")
        # step back
        driver.back()
        print("Go on step back in browser history.")
        # step forward
        driver.forward()
        print("Go on step forward in browser history.")
        # get page source
        page_source = driver.page_source
        print("Page source: " + page_source)
        # close browser/ quit browser
        # driver.quit()
        driver.close()


test_page = BrowserInteractions()
test_page.test()



