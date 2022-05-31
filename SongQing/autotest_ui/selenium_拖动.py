# -*- coding:utf-8 -*-
# @Time : 2022/5/18 15:37
# Auther : shenyuming
# @File : selenium_拖动.py
# @Software : PyCharm

'''
知识点:  location_once_scrolled_into_view  滚动到可见
        1. 在当前页可视范围内看不到的，也可能可以点的。
----------------------------------------------------
        value_of_css_property  获取元素的css属性值
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.runoob.com/')
sleep(2)
xpath = '//*[contains(text(),"网站建设指南")]'

test_flag = 2
if test_flag ==1:           # location_once_scrolled_into_view  滚动到xpath位置
    ele = driver.find_element_by_xpath(xpath).location_once_scrolled_into_view
    driver.find_element_by_xpath(xpath).click()

elif test_flag == 2:
    ele = driver.find_element_by_xpath(xpath)   #value_of_css_property 获得css的属性
    print('获得css的color',ele.value_of_css_property('color'))
    print('获得css的font-size',ele.value_of_css_property('font-size'))
sleep(2)
driver.quit()