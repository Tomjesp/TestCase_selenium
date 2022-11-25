import csv
import unittest
from time import sleep

from parameterized import parameterized

from chapter01.v3.base.get_driver import GetDriver
from chapter01.v3.page.PageLogin import PageLogin
from chapter01.v3.page.AddPage import addpage
#参数化
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=GetDriver().get_driver()
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()
    def test_login(self):
        self.login=PageLogin(self.driver)
        self.login.page_login("12","001","001","shtd")
        self.add.brand_btn_click()
        with open("brand_add.csv",encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                self.add.brand_add(row[0], row[1])
                self.add.brand_add_btn()