from chapter01.v3 import page
from chapter01.v3.base.base import Base


class PageLogin(Base):
    # 输入ID
    def page_input_login_id(self, id):
        self.base_input(page.login_Id, id)

    # 输入用户名
    def page_input_login_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_login_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_login_vericode(self, vericode):
        self.base_input(page.login_verity_code, vericode)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 组合业务
    def page_login(self, id, username, password, vericode):
        self.page_input_login_id(id)
        self.page_input_login_username(username)
        self.page_input_login_password(password)
        self.page_input_login_vericode(vericode)
        self.page_click_login_btn()
