# -*- coding:utf-8 -*-
# @Time : 2022/3/30 22:14
# Auther : shenyuming
# @File : selenium_xpath属性法.py
# @Software : PyCharm
'''
    xpath 属性法
    //*[@属性='值']  所有标签中 属性 = 值 的元素
    //input[@属性='值'] 所有input标签中 属性=值 的元素
    class 的值要写全部，
'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join('{}'.format('file://')+file_path,'text_b.html')
    driver.get(path)
    sleep(1)
    driver.find_element_by_xpath('//*[@class="ls_ssen vm"]').click()
    sleep(2)