# —— coding :utf-8 ——
# @time:    2020/9/16 1:08
# @IDE:     web_framework_v1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    login_datas.py
# 正常用例 -登录成功
success_data = {"user":"18684720553","password":"python"}

# 异常用例 - 错误的手机号格式(大于11位、小于11位、为空、不在号码段)
phone_data = [
    {"user":"1868472055","password":"python","check":"请输入正确的手机号"},  # 小于11位
    {"user":"186847205531","password":"python","check":"请输入正确的手机号"}, #大于11位
    {"user":"","password":"python","check":"请输入手机号"},  # 手机号为空
    {"user":"11684720553","password":"python","check":"请输入正确的手机号"} # 不在手机号段
]

wrongPwd_noReg_data = [
    {"user":"18684720553","password":"pytho","check":"帐号或密码错误!"},  # 密码错误
    {"user":"18684720550","password":"python","check":"此账号没有经过授权，请联系管理员!"}, # 账号没有授权
]
