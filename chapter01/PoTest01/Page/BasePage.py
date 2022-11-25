from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from chapter01.PoTest01 import Page


class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def find_locator(self,locator,timeout=30):
        return WebDriverWait(self.driver,timeout=timeout).until(lambda x:x.find_element(locator))
    def base_input(self,locator,value):
        self.find_locator(locator).send_keys(value)
    def base_click(self,locator):
        self.find_locator(locator)
    def base_alert(self,except_code):
        self.alert=self.driver.switch.to_alert
        self.alert.accept()
        self.assertEquals(except_code,self.alert.text)
    # def get_Driver(self):
    #     if self.driver==None:
    #         self.driver=webdriver.Chrome()
    #         self.driver.get(Page.URL)
    #         self.driver.implicitly_wait(5)
    # def quit_Driver(self):
    #     self.driver.quit()