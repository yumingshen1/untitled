# -*- coding:utf-8 -*-
# @Time : 2022/3/21 22:52
# Auther : shenyuming
# @File : selenium_tag.py
# @Software : PyCharm
'''
    标签定位 ，
    知识点tag  鸡肋，基本不用 (body中都可以， head不太适用，得不到文本)
'''

from selenium import webdriver
from pathlib import Path
from time import sleep
import os

# with webdriver.Chrome() as driver:
driver = webdriver.Chrome()
driver.get(r'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/test_a.html')
sleep(1)
ele = driver.find_element_by_tag_name('p')
ele2 = driver.find_element_by_tag_name('title')
## 获得 ele的可用方法
for _ in dir(ele):
    if _[0] != '_':
        print(_)

test_flage = 1

if test_flage ==1:
    print('p标签元素文本：',ele.text)
    print('p标签',ele.tag_name)
    print('title标签元素文本：',ele2.text)
    print('title标签',ele2.tag_name)

driver.quit()
