# —— coding :utf-8 ——
# @time:    2020/9/16 15:49
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    loginpage_locators.py

from selenium.webdriver.common.by import By
class LoginPageLocator:
    ''''元素定位类'''
    # 用户名输入框
    user_input = (By.XPATH,'//input[@name="phone"]')
    # 密码输入框
    pwd_input = (By.XPATH,'//input[@name="password"]')
    # 登录按钮
    login_but = (By.XPATH,'//button[text()="登录"]')
    # 错误提示框  ---登录区域
    get_errorMsg_from_login = (By.XPATH,'//div[@class ="form-error-info"]')
    # 密码错误、没有注册、没有输入验证码中间提示框
    get_login_wrongPwd_noReg = (By.XPATH,'//div[@class="layui-layer-content"]')