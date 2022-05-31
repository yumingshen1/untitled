# -*- coding:utf-8 -*-
# @Time : 2022/5/31 17:28
# Auther : shenyuming
# @File : 键盘模块.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

'''
知识点:
send_keys 发送按键
组合键发送用 Key.Control,'A'
按键去区分大小写
元素上发送的按键有别于 网页上的按键（用第三方模块实现，如pyautogui）
'''

driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
sleep(2)
#输入
driver.find_element_by_css_selector('#ls_username').send_keys('admin')
sleep(2)
#全选 control+A
driver.find_element_by_css_selector('#ls_username').send_keys(Keys.CONTROL,'A')
sleep(2)
# 复制 control+c
driver.find_element_by_css_selector('#ls_username').send_keys(Keys.CONTROL,'c')
sleep(2)
#找到输入框    \ue009 == Keys.CONTROL
driver.find_element_by_css_selector('#scbar_txt').send_keys('\ue009','V')
sleep(2)
#删除部分数据min
driver.find_element_by_css_selector('#scbar_txt').send_keys(Keys.BACKSPACE*3)
sleep(2)
#搜索
driver.find_element_by_css_selector('#scbar_btn').click()
sleep(2)
driver.quit()
