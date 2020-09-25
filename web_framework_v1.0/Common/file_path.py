# —— coding :utf-8 ——
# @time:    2020/9/17 15:11
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    file_path.py
import os
# base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] 二选1
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_path,"TestDatas")

testcases_dir = os.path.join(base_path,"TestCases")

htmlreport_dir = os.path.join(base_path,"OutPuts/reports")
screenshots_path = os.path.join(base_path,'OutPuts/screenshots')
logs_path = os.path.join(base_path,'OutPuts/logs')

# config_dir = os.path.join(base_path,'Config')

