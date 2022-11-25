import csv
import unittest

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class d32(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://192.168.111.128/bsams/front/login.do?")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def test_01(self):
        element=self.driver.find_element(By.ID,"taskId")
        element.clear()
        element.send_keys("12")
        element=self.driver.find_element(By.ID,"loginName")
        element.clear()
        element.send_keys("001")
        element=self.driver.find_element(By.ID,"password")
        element.clear()
        element.send_keys("001")
        element=self.driver.find_element(By.ID,"vericode")
        element.clear()
        element.send_keys("shtd")
        element.find_element(By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div[6]/input").click()
        self.driver.refresh()
        sleep(3)
        element=self.driver.find_element(By.ID,"leftmenu_asset_discard").click()
        with open("brand_add.csv",encoding='UTF-8') as f:
            f_csv=csv.reader(f)
            next(f_csv)
            for row in f_csv:
                element=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[1]/div/input").click()
                element=self.driver.find_element(By.ID,"title").send_keys(row[0])
                element=self.driver.find_element(By.ID,"code").send_keys(row[1])
                element=self.driver.find_element(By.LINK_TEXT,"保存").click()
                alert=self.driver.switch_to.alert
                alert.accept()
                self.assertEquals("保存成功",alert.text)
    def tearDown(self) -> None:
        self.driver.close()
if  __name__=='_main_':
      unittest.main()