# -*- coding:utf-8 -*-
# @Time : 2022/5/11 22:52
# Auther : shenyuming
# @File : selenium_css高级.py
# @Software : PyCharm
'''
    div p   div下的标签（子孙） //div//p
    div>p   div下的p (儿子)     //div/p
    p+input     p标签同级下的input，且紧挨着
    属性：
        [属性=属性值]
    没有函数：
        [属性^=属性值]  开头是。。。
        [属性*=属性值]  包含。。。
        [属性$=属性值]  结尾是。。。
'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join('file://'+file_path,'test_a.html')
    driver.get(url=path)
    sleep(1)
    driver.find_element_by_css_selector('.vp.vm').send_keys('xxxx')
    driver.find_element_by_css_selector('[id^="xxx_y"]').click()