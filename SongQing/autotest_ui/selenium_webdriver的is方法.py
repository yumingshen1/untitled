# -*- coding:utf-8 -*-
# @Time : 2022/5/18 12:27
# Auther : shenyuming
# @File : selenium_webdriver的is方法.py
# @Software : PyCharm
'''
知识点:
is_displayed  是否显示   hidden='hidden'
is_enabled    是否使能   disabled=''
is_selected   是否选中   type="radio"
'''
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = os.path.dirname(__file__)
path = os.path.join('file://'+file_path,'test_b.html')
driver.get(path)
ele_alert = driver.find_element_by_id('alert')
print('alert按钮是否显示: ',ele_alert.is_displayed())  #FALSE

ele_confirm = driver.find_element_by_id('confirm1')
print('confirm按钮是否使能: ',ele_confirm.is_enabled())  #FALSE

ele_radio = driver.find_element_by_id('radio')
print('radio是否选中',ele_radio.is_selected())  #false
ele_radio.click()
print('radio是否选中',ele_radio.is_selected())  #true

driver.quit()


