# -*- coding:utf-8 -*-
# @Time : 2022/5/17 15:19
# Auther : shenyuming
# @File : selenium_css数字开头.py
# @Software : PyCharm

'''
数字开头的id
'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join('file://'+file_path,'test_c.html')
    driver.get(url=path)
    sleep(2)
    # 错误：An invalid or illegal selector was specified
    # 解决：到页面赋值copy selector 然后加个转义得到#\\39 XPMF
    driver.find_element_by_css_selector('#\\39XPMF').send_keys('admin')
    driver.find_element_by_css_selector('#PXXXM').send_keys('123456')
    sleep(2)