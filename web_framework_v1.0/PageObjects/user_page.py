# —— coding :utf-8 ——
# @time:    2020/9/16 19:46
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    user_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UserPage:
    "投资页面"
    def __init__(self,driver):
        self.driver = driver
    # 用户个人信息操作
    def user_info(self):
        pass
    def click_recharge_button(self):
        pass
    def click_withdraw_button(self):
        pass

    def click_my_zipei_button(self):
        pass
    def click_invest_project_button(self):
        pass
    def click_return_money_button(self):
        pass
    def click_rewards_record_button(self):
        pass
    def get_user_leftMoney(self):
        pass

