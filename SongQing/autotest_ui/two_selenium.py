# -*- coding:utf-8 -*-
# @Time : 2022/3/21 22:52
# Auther : shenyuming
# @File : two_selenium.py
# @Software : PyCharm
'''
    标签定位
'''

from selenium import webdriver
from pathlib import Path
from time import sleep
import os

with webdriver.Chrome() as driver:
    driver.get(r'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/test_a.html')
    sleep(1)
    ele = driver.find_element_by_tag_name('p')
    for _ in dir(ele):  ## 获得 ele的可用方法
        if _[0] != '_':
            print(_)
