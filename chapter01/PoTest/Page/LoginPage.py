from chapter01.PoTest.Page.BasePage import base
from chapter01.PoTest import Page


class LoginPage(base):
    # 输入ID
    def base_input_id(self, id):
        self.base_input(Page.login_Id,id)

    # 输入username
    def base_input_username(self, username):
        self.base_input(Page.login_username,username)

    # 输入密码
    def base_input_pwd(self, pwd):
        self.base_input(Page.login_pwd,pwd)

    # 输入验证码
    def base_input_vericode(self, vericode):
        self.base_input(Page.login_vericode,vericode)
    # 点击登录按钮
    def base_login_click_btn(self):
        self.base_find_loc(Page.login_btn).click()

    # 集合
    def page_login(self, id, username, pwd, vericode):
        self.base_input_id(id)
        self.base_input_username(username)
        self.base_input_pwd(pwd)
        self.base_input_vericode(vericode)
        self.base_login_click_btn()
