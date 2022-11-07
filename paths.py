import os


class Paths:
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, "chromedriver/chromedriver.exe")
