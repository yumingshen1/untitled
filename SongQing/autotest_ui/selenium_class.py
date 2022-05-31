# -*- coding:utf-8 -*-
# @Time : 2022/3/30 20:51
# Auther : shenyuming
# @File : selenium_class.py
# @Software : PyCharm

'''
    class属性定位
    一个元素内有多个值，只写一个   class = 's_de cv' ,  只取s_de 或  cv，    如果硬要区全部可还是用 s_de.cv
'''
from selenium import webdriver
from pathlib import Path
from time import sleep
import os

driver = webdriver.Chrome()
path = os.path.dirname(__file__)
pt = os.path.join('{}'.format('file://')+path,'test_a.html')
driver.get(pt)
driver.find_element_by_class_name('aa').send_keys('用户名')
driver.find_element_by_class_name('bb').send_keys('pass')
driver.find_element_by_class_name('cc').send_keys('word')
sleep(2)
driver.find_element_by_class_name('bb.cc').send_keys('加一个 。')  ## calss_name如果写全部的值中间加一个 .
sleep(2)
driver.quit()