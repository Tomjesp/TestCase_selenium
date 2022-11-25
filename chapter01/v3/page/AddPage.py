import time

from chapter01.v3.base import base
from selenium import webdriver
from chapter01.v3 import page
from time import sleep

from chapter01.v3.base.base import Base


class addpage(Base):
    # 点击品牌按钮
    def brand_btn_click(self):
        self.base_find_element(page.brand_btn).click()

    # 点击新增按钮
    def brand_add_btn(self):
        self.base_find_element(page.add_btn).click()

    # 输入品牌名称，编码
    def brand_add(self, title, code):
        time.sleep(2)
        self.brand_add_btn()
        self.base_find_element(page.brand_name).send_keys(title)
        self.base_find_element(page.brand_code).send_keys(code)
        self.base_find_element(page.brand_add_preservation).click()
        sleep(1)
        self.alert = self.driver.switch_to.alert
        self.alert.text
        self.alert.accept()
        sleep(2)
