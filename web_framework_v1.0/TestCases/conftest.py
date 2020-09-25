# —— coding :utf-8 ——
# @time:    2020/9/18 2:12
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py

from selenium import webdriver
from TestDatas import Common_datas as CD
from PageObjects.login_page import LoginPage
import pytest

driver = None
# 声明是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    print("所有用例执行之前，setup整个测试类执行一次")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver,lg)  # 分割线：返回值
    # 后置操作
    print("所有用例执行完成，tearDown整个测试类执行一次")
    driver.quit()

@pytest.fixture
def refresh_page():
    global  driver
    # 前置操作
    yield
    # 后置操作
    driver.refresh()

@pytest.fixture(scope="session")
def session_demo():
    print("整个测试会话期间开始")
    yield
    print("整个测试会话期间的结束")

@pytest.fixture(scope="class")
def class_demo():
    print("整个测试会话期间开始")
    yield
    print("整个测试会话期间的结束")


@pytest.fixture
def func_demo():
    print("整个测试会话期间开始")
    yield
    print("整个测试会话期间的结束")