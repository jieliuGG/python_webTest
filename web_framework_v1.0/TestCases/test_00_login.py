# —— coding :utf-8 ——
# @time:    2020/9/15 15:10
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_00_login.py
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
import ddt
from TestDatas import Common_datas as CD
from TestDatas import login_datas as LD
import pytest

@pytest.mark.demo
@pytest.mark.usefixtures("class_demo")
@pytest.mark.usefixtures("func_demo")
def test_dome():
    demo()
    assert False

def demo():
    print("把test_demo加到demo装饰器中进行修饰")
    print("修饰完成后返回给test_demo")

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin():
    # TestCase中不能写__init__
    # @classmethod
    # def setUpClass(cls):
    #     #通过excel读取本功能当中需要的所有测试数
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    # # def setUp(self):
    # #     pass
    # def tearDown(self):
    #     '''后置'''
    #     # 正常用例 -登录成功
    #     self.driver.refresh()

    # 异常用例 - 错误的手机号格式(大于11位、小于11位、为空、不在号码段) ddt
    @pytest.mark.parametrize("data",LD.phone_data)  # 参数化，把LD.phone_data的测试数据交给自定义参数名为data的参数
    def test_login_0_user_wrongFormat(self, data,access_web):
        # 步骤 输入用户名:xxx,密码：xxx,点击登录
        access_web[1].login(data["user"],data["password"])
        # 断言 登录页面 提示：请输入正确手机号
        # 对别文件内容与期望值是否相等
        assert (access_web[0].get_errorMsg_from_loginArea(), data["check"])

    # 手机号没有注册
    @pytest.mark.parametrize("caseData",LD.wrongPwd_noReg_data)
    def test_login_1_wrongPwd_noReg(self,caseData,):
        # 步骤：输入用户名：xxx， 密码：xxx 点击登录
        self.lg.login(caseData["user"],caseData["password"])
        # 断言： 登录页面 页面中间提示：此账号没有经过授权，请联系管理员! / 密码错误
        # 登录页面中， --获取提示框文本内容
        # 对比文本内容与期望值是否相等
        self.assertEqual(self.lg.get_login_wrongPwd_noRegArea(),caseData["check"])

    # fixture的函数名称用来接收它的返回值
    @pytest.mark.smoke
    def test_login_2_normal(self,access_web):
        # 步骤 输入用户名:xxx,密码：xxx,点击登录
        access_web[1].login(LD.success_data["user"], LD.success_data["password"])
        # 断言 首页当中能找到“我的帐户”或“退出"关键字
        assert  IndexPage(access_web[0]).isExist_logout_ele()

    # # 异常用例 - 错误密码
    # def test_wrong_pwd(self):
    #     # 步骤 输入用户名:xxx,密码：xxx,点击登录
    #     self.lg.login("18684720553", "python11")
    #     # 断言 首页当中能找到“我的帐户”或“退出"关键字
    #     self.assertTrue(IndexPage(self.driver).isExist_logout_ele())
    # # 异常用例 - 不输入密码
    # def test_No_pwd(self):
    #     # 步骤 输入用户名:xxx,密码：xxx,点击登录
    #     self.lg.login("18684720553", "")
    #     # 断言 首页当中能找到“我的帐户”或“退出"关键字
    #     self.assertTrue(IndexPage(self.driver).isExist_logout_ele())


if __name__ == '__main__':
    pass
