# -*- coding:utf-8 -*-
# @Time : 2022/5/18 11:39
# Auther : shenyuming
# @File : selenium_find_elements.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

'''
    find_elements 返回一个列表
'''
with webdriver.Chrome() as driver:
    url =  'http://www.baidu.com'
    driver.get(url)                 #找到相同元素，定位相同的元素全部循环出来
    ele_hots = driver.find_elements_by_css_selector('.title-content-title')
    for con in ele_hots:
        print(con.text)