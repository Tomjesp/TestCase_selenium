import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class test01(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.get("http://192.168.111.128/bsams/front/login.do?")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def find_loc(self,timeout=30,*loc):
        return WebDriverWait(self.driver,timeout=timeout).until(lambda x:x.find_element(*loc))
    def test_01(self):
        self.find_loc(By.ID,"taskId").send_key("12")
    def tearDown(self) -> None:
        self.driver.close()
if __name__=='_main_':
    unittest.main()
