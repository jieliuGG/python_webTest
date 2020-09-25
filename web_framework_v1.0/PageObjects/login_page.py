# —— coding :utf-8 ——
# @time:    2020/9/15 15:10
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    login_page.py

from PageLocators.loginpage_locators import LoginPageLocator as loc
from Common.base_page import BasePage

class LoginPage(BasePage):
    '''登录页面类'''
    # 登录操作
    def login(self, username, password, remember_user=True):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.user_input,doc=doc)
        self.input_text(loc.user_input,username,doc)
        self.input_text(loc.pwd_input,password,doc)
        # 判断remember_user的值，决定是否勾选
        self.click_element(loc.login_but,doc)

    # 获取错误提示信息 ----登录区域
    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_获取登录区域错误提示信息"
        self.wait_eleVisible(loc.get_errorMsg_from_login,doc=doc)
        return self.get_eleText(loc.get_errorMsg_from_login,doc)

    # 获取错误提示信息---中间区域
    def get_login_wrongPwd_noRegArea(self):
        doc = "登录页面_获取中间区域错误提示信息"
        self.wait_eleVisible(loc.get_login_wrongPwd_noReg,poll_frequency=0.2,doc=doc) # 错误的密码和没有注册提示信息在中间区域显示
        return self.get_eleText(loc.get_login_wrongPwd_noReg,doc)

    def register(self):
        pass

