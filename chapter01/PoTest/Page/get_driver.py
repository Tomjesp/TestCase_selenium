from selenium import webdriver
from chapter01.PoTest import Page
class GetDriver:
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver==None:
            cls.driver=webdriver.Chrome()
            cls.driver.implicitly_wait(5)
            cls.driver.maximize_window()
            cls.driver.get(Page.url)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
