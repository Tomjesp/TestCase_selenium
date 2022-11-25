from datetime import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from chapter01.PoTest import Page


class base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_loc(self, loc, timeout=30):
        return WebDriverWait(self.driver, timeout=timeout).until(lambda x: x.find_element(loc))

    def base_input(self, loc, value):
        element=self.base_find_loc(loc)
        element.clear()
        element.send_keys(value)
    # 截图
    def base_getScreenShoot(self):
        self.driver.get_srceenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
