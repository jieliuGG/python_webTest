# —— coding :utf-8 ——
# @time:    2020/9/17 0:40
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    indexpage_locators.py
from selenium.webdriver.common.by import By
# 用户名
user_link = (By.XPATH,'//a[@href="/Member/index.html"]')
# 投标按钮
bid_button = (By.XPATH,'//*[text()="抢投标"]')    #//a[@class="btn btn-special"]