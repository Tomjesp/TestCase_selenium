from chapter01.PoTest.Page.BasePage import base
from selenium import webdriver
from chapter01.PoTest import Page
from time import sleep
class AddPage(base):
    #点击品牌按钮
    def brand_btn_click(self):
        self.base_find_loc(Page.brand_btn).click()
    #点击新增按钮
    def brand_add_btn(self):
        self.base_find_loc(Page.add_btn).click()
    #输入品牌名称，编码
    def brand_add(self,title,code):
        self.brand_add_btn()
        self.base_find_loc(Page.brand_name).send_keys(title)
        self.base_find_loc(Page.brand_code).send_keys(code)
        self.base_find_loc(Page.brand_add_preservation).click()
        self.alert=self.driver.switch_to.alert
        sleep(3)
        try:
            self.assertEqual(self.alert.text,"保存成功！")
            sleep(1)
        except AssertionError:
            self.base_getScreenShoot()
            sleep(1)
            raise
        finally:
            self.alert.accept()

    def assertEqual(self, text, param):
        pass
