# —— coding :utf-8 ——
# @time:    2020/9/16 19:45
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    bid_page.py
from Common.base_page import BasePage
from PageLocators import investpage_locators as loc


class BidPage(BasePage):
    "投资页面"

    # 投资
    def invest(self, money):
        # 在输入框当中，输入金额
        # 点击投标按钮
        doc = "标详情页面_投资操作"
        self.wait_eleVisible(loc.money_input,doc=doc)
        self.input_text(loc.money_input,money,doc) # 获取元素已经封装在每个方法中
        # 点击投标按钮
        self.click_element(loc.invest_button,doc)


    # 获取用户余额
    def get_user_money(self):
        doc = "投资页面_获取用户余额"
        self.wait_eleVisible(loc.money_input,doc=doc)
        return self.get_element_attribute(loc.money_input,"data-amount",doc)

    # 点击成功的提示框 - 点击查看并激活
    def click_activeButton_on_success_popup(self):
        doc = "投资页面_点击成功的提示框"
        self.wait_eleVisible(loc.active_button_on_success_pop,doc=doc)
        return self.click_element(loc.active_button_on_success_pop,doc)

    # 错误提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        doc = "投资页面_页面中间的错误提示框信息"
        # 获取文本内容
        self.wait_eleVisible(loc.invest_failed_popup,doc=doc)
        msg = self.get_eleText(loc.invest_failed_popup,doc)
        self.switch_to_alert(loc.invest_failed_popup,doc)
        return msg

    # 获取提示信息  - 投标按钮上的
    def get_errorMsg_from_investButton(self,text):
        doc = "投资页面_投资按钮上的提示信息"
        self.wait_eleVisible(loc.errorMsg_from_investButton,doc=doc)
        return self.get_eleText(loc.errorMsg_from_investButton,text,doc)


