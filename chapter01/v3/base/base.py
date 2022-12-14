import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        msg = self.base_find_element(*loc).text
        return msg

    # 截图
    def base_getScreenShoot(self):
        self.driver.get_srceenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
