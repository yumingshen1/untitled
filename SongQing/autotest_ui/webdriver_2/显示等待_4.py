# -*- coding:utf-8 -*-
# @Time : 2022/6/3 22:46
# Auther : shenyuming
# @File : 显示等待_4.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
''' 
知识点:  title_is  判断网页title是否特定文本
1. 源码分析 
2. 传参    title   ；判断浏览器操作之后的浏览器的TITLE是否等于传入的TITLE
3. 返回值  T/F
'''

driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
driver.find_element_by_css_selector('#ls_username').send_keys('admin')
driver.find_element_by_css_selector('#ls_password').send_keys('123456')
driver.find_element_by_css_selector('#ls_password').submit()
excepted_title = '论坛 - Powered by Discuz!'
try:
    WebDriverWait(driver,10,1).until(EC.title_is(excepted_title))
    print('title一致')
except:
    print('title不一致')
sleep(2)
driver.quit()