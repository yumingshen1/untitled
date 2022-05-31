# -*- coding:utf-8 -*-
# @Time : 2022/5/31 16:40
# Auther : shenyuming
# @File : select操作.py
# @Software : PyCharm
'''
知识点：select
可以直接点击
推荐使用selenium提供的模块
定位方法：
    by_index  下标 0开始
    by_value  value属性值
    by_visible_text  >文本<
    deselect_all  反选所有
    全选没有，要自己实现
'''
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
path = os.path.dirname(__file__)
path1 = path.split('webdriver_1')[0]
path2 = os.path.join('{}'.format('file://') + path1, 'test_a.html')
driver.get(path2)

test_flage=1

if test_flage ==1:
    #获得外层element
    ele_select = driver.find_element_by_css_selector('#id6>select')
    #获得所有的子项
    ele_option = driver.find_elements_by_css_selector('select option')
    for option in ele_option:   #循环子项
        sleep(1)
        Select(ele_select).select_by_visible_text(option.text)  #选择每一个子项--全选
    sleep(2)
    Select(ele_select).deselect_all()   #反选全部
    sleep(2)
    driver.quit()

if test_flage ==3:
    sle_select = driver.find_element_by_css_selector('#id6>select')
    Select(sle_select).select_by_index('1') #索引
    sleep(2)
    Select(sle_select).select_by_value('3') #value值
    sleep(2)
    Select(sle_select).select_by_visible_text('30k-35k') # 文本
    sleep(2)
    driver.quit()

if test_flage ==2:
    driver.find_element_by_css_selector('#id6 option:nth-child(2)').click()
    sleep(2)
    driver.quit()