import HTMLTestRunner
from Common.file_dir import *
import unittest
from Common import file_dir
import pytest
# 实例化套件对象
s = unittest.TestSuite()
# 1. 实例化TestLoader对象
loader = unittest.TestLoader()
# 2. 使用discover找到一个目录下所有测试用例
s.addTests(loader.discover(TestCases_path))
fp = open(reports_path+'autoTest_report.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='单元测试报告',
    description='web自动化单元测试报告',
)
runner.run(s)

# 运行方式2
# pytest.main([
#              # "-m invest",
#              "--html={0}/report.html".format(file_dir.reports_path),
#              "--junitxml={0}/report.xml".format(file_dir.reports_path),
#              "--alluredir={0}".format(file_dir.allure_reports_path),
#              "--reruns","2","--reruns-delay","5"]
# )
