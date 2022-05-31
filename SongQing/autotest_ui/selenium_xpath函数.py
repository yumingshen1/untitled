# -*- coding:utf-8 -*-
# @Time : 2022/3/31 21:15
# Auther : shenyuming
# @File : selenium_xpath函数.py
# @Software : PyCharm
'''
    xpath 函数法：
starts-with (@属性,属性开头的值)
contains (@属性,属性包含的值)
ends-with (@属性,属性结尾的值)
text()='文本值' #替代link_text
contains(text(),文本包含的值) #替代partial_link_text

示例:
//p[@text()='xxx']
//p[contains(text(),'xxx')]
//input[starts-with(@id,'xxx')]
'''

from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join('{}'.format('file://') + file_path, 'test_b.html')
    driver.get(path)
    driver.find_element_by_xpath("//*[starts-with(@id,'ale')]").click() #所有的标签下，id值以ale开头的元素
    sleep(2)

