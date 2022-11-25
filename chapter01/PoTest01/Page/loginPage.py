from chapter01.PoTest01 import Page
from chapter01.PoTest01.Page.BasePage import BasePage


class loginPage(BasePage):
    def get_login(self,id,username,pwd,vericode):
        #ID
        self.base_input(Page.LOGIN_ID,id)
        #username
        self.base_input(Page.LOGIN_NAME,username)
        #pwd
        self.base_input(Page.LOGIN_PWD,pwd)
        #vericode
        self.base_input(Page.LOGIN_VERICODE,vericode)
        #LOGIN_BTN
        self.base_click(Page.LOGIN_BTN)
