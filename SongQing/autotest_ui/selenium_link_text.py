# -*- coding:utf-8 -*-
# @Time : 2022/3/30 21:01
# Auther : shenyuming
# @File : selenium_link_text.py
# @Software : PyCharm
'''
    link_text 两种定位
    只适用于 a标签的文本
    link_text  完全匹配
    parti_link_text 模糊匹配
'''
from selenium import webdriver
from pathlib import Path
from time import sleep
import os

driver = webdriver.Chrome()
path = os.path.dirname(__file__)
pt = os.path.join('{}'.format('file://')+path,'test_a.html')
driver.get(pt)

# driver.find_element_by_link_text('有求必应').click()
driver.find_element_by_partial_link_text('百度').click()

sleep(1)
driver.quit()