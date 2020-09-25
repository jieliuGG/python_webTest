# —— coding :utf-8 ——
# @time:    2020/9/16 17:16
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_01_invest.py
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
import unittest
import ddt
from TestDatas import Common_datas as CD
from PageObjects.bid_page import BidPage
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.user_page import UserPage
from TestDatas import invest_datas as ID
from TestDatas import login_datas as LD

@ddt.ddt
class TestInvest(unittest.TestCase):
    '''测试投资类'''

    @classmethod
    def setUpClass(cls):
        # 初始化浏览器会话
        # 通过excel读取本功能当中需要的所有测试数
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.web_login_url)
        LoginPage(cls.driver).login(LD.success_data["user"], LD.success_data["password"])
        # 1. 在首页投资 ---不根据标名，根据抢投标。默认第一个表
        IndexPage(cls.driver).click_first_bid()
        cls.bid_page = BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        time.sleep(0.3)

    # def setUp(self):
    #     pass
    def tearDown(self):
        '''后置'''
        # 正常用例 -登录成功
        self.driver.refresh()

    @pytest.mark.smoke
    def test__invest_success(self):
        # 正常用例 前提条件
        # 用户已登录
        # 有能够投资的标
        # 账号有余额可以投资
        # 步骤
        # 标页面---获取一下投资用户余额
        userMoney_beforeInvest = self.bid_page.get_user_money()

        # 2. 标页面---输入投资金额，点击投资按钮
        self.bid_page.invest(ID.invest_money_seccess["money"])
        # 3. 标页面---点击投资成功的弹出框--查看并激活
        self.bid_page.click_activeButton_on_success_popup()
        # 断言
        # 个人页面----获取投资后金额
        userMoney_afterInvest = UserPage(self.driver).get_user_leftMoney()
        # 投资前金额-投资后金额  = 投资金额
        assert ID.invest_money_seccess['money'] == int(float(userMoney_beforeInvest)-float(userMoney_afterInvest))

    @ddt.data(*ID.invert_money_no100)
    def test_invest_0_fail_no100(self,data):
        # 标页面---获取一下投资用户余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标签面 - 输入投资金额，点击投标按钮
        self.bid_page.invest(data["money"])
        # 获取提示信息
        errorMsg = self.bid_page.get_errorMsg_from_pageCenter()
        # 刷新
        self.driver.refresh()
        # 获取用户余额
        userMoney_afterInvest = self.bid_page.get_user_money()
        # 断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest
    def test_invest_1_fail_no10(self):
        pass
