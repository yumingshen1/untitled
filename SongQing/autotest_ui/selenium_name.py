# -*- coding:utf-8 -*-
# @Time : 2022/3/26 17:36
# Auther : shenyuming
# @File : selenium_name.py
# @Software : PyCharm

'''
    name属性值定位
'''


from selenium import webdriver
from pathlib import Path
from time import sleep
import os

driver = webdriver.Chrome()
path = os.path.dirname(__file__)
pt = os.path.join('{}'.format('file://')+path,'test_a.html')
driver.get(pt)
driver.find_element_by_name('username').send_keys('名字')
sleep(2)
driver.quit()
