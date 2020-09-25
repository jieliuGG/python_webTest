# —— coding :utf-8 ——
# @time:    2020/9/17 11:37
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    base_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Common import file_path
# 封装基本函数---执行日志、异常处理、失败截图
# 所有页面公共部分
import logging
import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, timeout=30, poll_frequency=0.5, doc=""):
        """

        :param locator: 元素定位，元组形式。 (元素类型,元素定位方式)
        :param timeout:
        :param poll_frequency:
        :param doc: 模块名称_页面名称_操作名称
        :return:
        """
        logging.info("等待元素可见{}可见".format(locator))
        try:
            # 开始等待时间点
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志当中，等待了多久  差值转换为秒
            wait_times = (end - start).seconds
            logging.info("{0}:元素:{1}已可见，等待起始时间：{2}，等待结束时间：{3}，等待时间：{4}".format(doc,locator,start,end,wait_times))
        except:
            # 捕获异常到日志中
            logging.exception("等待元素可见异常")
            # 截图 - 保存到指定目录
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("{0}查找元素：{1}".format(doc,locator))
        # 查找元素
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 点击操作
        logging.info("{0}点击元素:{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        logging.info("{0}元素{1},输入内容为:{2}".format(doc,locator,text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败")
            self.save_screenshot(doc)
            raise

    # 获取元素文本
    def get_eleText(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}获取元素：{1}的文本内容".format(doc, locator))
        # 获取文本
        try:
            text = ele.text
            logging.info("元素：{0}的文本内容为：{1}".format(locator,text))
            return text
        except:
            logging.exception("获取元素文本内容失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_element_attribute(self, locator, attribute, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}获取元素：{1}的属性：{2}".format(doc, locator,attribute))
        # 获取属性
        try:
            ele_attr = ele.get_attribute(attribute)
            logging.info("元素：{0}的属性{1} 值为：{2}".format(locator,attribute,ele_attr))
            return ele_attr
        except:
            logging.exception("获取元素属性值失败！")
            self.save_screenshot(doc)
            raise

    # alert处理
    def switch_to_alert(self, timeout=30, poll_frequency=0.5, model=None):
        logging.info("{0}_切换alert弹窗".format(model))
        try:
            return WebDriverWait(timeout, poll_frequency).until(EC.alert_is_present())
        except:
            logging.exception("{0}_切换alert弹窗失败".format(model))
            self.save_screenshot(model)
            raise

    # 判断元素是否存在
    def ele_isExist(self,locator,timeout=10,doc=""):
        logging.info("{}中是否存在元素：{}".format(doc,locator))
        try:
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            logging.info("{0}秒内页面{1}存在中存在元素：{2}".format(timeout,doc,locator))
            return True
        except:
            logging.exception("{0}秒内页面{1}存在中不存在元素：{2}".format(timeout,doc,locator))
            return False

    # iframe 切换
    # def switch_to_frame(self, frame_reference, timeout=30, poll_frequency=0.5, model=None):
    #     logging.info("{0}_切换iframe".format(model))
    #     try:
    #         WebDriverWait(timeout, poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))
    #     except:
    #         logging.exception("{0}_切换iframe".format(model))
    #         self.save_screenshot(model)
    #         raise

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    def scrollbar_handle(self):
        pass

    # 窗口切换
    # def switch_to_window(self, window_reference, timeout=30, poll_frequency=0.5, window_handles=None, model=None):
    #     '''
    #
    #     :param window_reference:
    #     :param timeout:
    #     :param poll_frequency:
    #     :param model:
    #     :return:
    #     '''
    #     logging.info("{0}_切换窗口".format(model))
    #     try:
    #         if window_reference == "new":
    #             if window_handles:
    #                 WebDriverWait(timeout, poll_frequency).until(EC.new_window_is_opened(window_handles))
    #                 current_window_handles = self.driver.window_handles
    #                 self.driver.switch_to.window(current_window_handles[-1])
    #             else:
    #                 logging.exception("打开新窗口时，请传入window_handles参数")
    #                 raise ("打开新窗口时，请传入window_handles参数")
    #         elif window_reference == "default":
    #             self.driver.switch_to.default_content()
    #         else:
    #             self.driver.switch_to.window(window_reference)
    #         logging.info("{0}_切换窗口成功".format(model))
    #     except:
    #         logging.exception("{0}_切换窗口失败".format(model))
    #         self.save_screenshot(model)
    #         raise

    # 保存截图
    def save_screenshot(self, doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        # filePath = "截图路径" + "{0}".format(time.strftime("%Y%m%d%H%M%S"))
        filePath = file_path.screenshots_path + \
                   "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为:{}".format(filePath))
        except:
            logging.exception("等待元素可见失败")
