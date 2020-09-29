# —— coding :utf-8 ——
# @time:    2020/9/30 2:18
# @IDE:     webTest_framewokv2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    save_img.py


from Common import file_dir
import time
import logging




def save_img(driver,model=None):
    logging.info("用例失败截图:{0}".format(model))
    try:
        filename = file_dir.screenshots_path+"\{0}_{1}.png".format(model,time.strftime("%Y%m%d%H%M%S"))
        driver.save_screenshot(filename)
        logging.info("截图文件：{0}".format(filename))
    except:
        logging.info("截图失败!!!")
        raise