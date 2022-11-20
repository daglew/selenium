
from selenium import webdriver
from selenium.webdriver.common.by import By
from paths import Paths


class Helpers:
    def __init__(self, driver):
        self.driver = driver
