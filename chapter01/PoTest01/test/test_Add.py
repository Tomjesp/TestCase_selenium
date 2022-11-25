import unittest

from parameterized import parameterized
from selenium import webdriver

from chapter01.PoTest01 import Page
from chapter01.PoTest01.Page.BasePage import BasePage
from chapter01.PoTest01.Page.loginPage import loginPage
#
# class teat_Add(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get(Page.URL)
#         self.driver.implicitly_wait(5)
#     def test_LOGIN(self):
#         self.login=loginPage(self.driver)
#         self.login.get_login("12","001","001","shtd")
#     def tearDown(self):
#         self.driver.close()
# if  __name__=='_main_':
#     unittest.main()
def test_login():
    driver=webdriver.Chrome()
    driver.get(Page.URL)
    driver.implicitly_wait(5)
    test_login=loginPage(driver)
    test_login.get_login("12","001","001","shtd")