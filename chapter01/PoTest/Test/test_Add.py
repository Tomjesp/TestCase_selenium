from parameterized import parameterized
import unittest

from parameterized import parameterized

from chapter01.PoTest.Page.LoginPage import LoginPage
from chapter01.PoTest.Page.get_driver import GetDriver


def get_data():
    return [("12","001","001","shtd")]
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #实例化driver
        cls.driver=GetDriver().get_driver()
        #实例化获取登录对象
        cls.login=LoginPage(cls.driver)
        #实例化AddPage对象
        #cls.add=AddPage(cls.driver)
    @classmethod
    def tearDown(cls):
        GetDriver().quit_driver()
    @parameterized.expand(get_data())
    def test_login(self,id,username,pwd,vericode):
        #调用登录方法
        self.login.page_login(id,username,pwd,vericode)
        #调用AddPage
        #self.add.brand_btn_click()
        #with open("brand_add.csv",encoding="gb2312") as f:
          #  reader = csv.reader(f)
           # for row in reader:
            #    self.add.brand_add(row[0],row[1])