# —— coding :utf-8 ——
# @time:    2020/9/27 14:28
# @IDE:     webTest_framewokv2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    file_dir.py
import os

# base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] 二选1
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试数据路径
TestDatas_path = os.path.join(base_path, 'TestDatas')

# 测试用例路径
TestCases_path = os.path.join(base_path, 'TestCases')

# 报告路径
reports_path = os.path.join(base_path, r'Outputs\reports')
allure_reports_path = os.path.join(base_path,r'Outputs\allure_reports')

# 截图路径
screenshots_path = os.path.join(base_path, r'Outputs\screenshots')

# 日志路径
logs_path = os.path.join(base_path, r'Outputs\logs')

# config_dir = os.path.join(base_path,'Config')

if __name__ == '__main__':
    print(logs_path)