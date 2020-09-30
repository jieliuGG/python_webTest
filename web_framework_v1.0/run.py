# —— coding :utf-8 ——
# @time:    2020/9/19 14:49
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    run.py
import HTMLTestRunner
from  Common.file_path import *
import unittest
# 实例化套件对象
s = unittest.TestSuite()
# 1.实例化TestLoader对象
# 2. 使用discover找到一个目录下所有测试用例
# 使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))
# # 运行
# runner = unittest.TextTestRunner()
# runner.run()

fp = open(htmlreport_dir+'/autoTest_report.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="单元测试报告",
        description="单元测试报告"

)
runner.run(s)