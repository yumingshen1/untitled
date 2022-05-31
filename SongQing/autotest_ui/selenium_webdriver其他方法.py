# -*- coding:utf-8 -*-
# @Time : 2022/5/18 14:43
# Auther : shenyuming
# @File : selenium_webdriver其他方法.py
# @Software : PyCharm


'''
知识点:
get_attribute  获取指定元素的属性的值
location
size
location
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
ele_user = driver.find_element_by_id('ls_username')
print('size:',ele_user.size)  #{'height': 23, 'width': 154}
print('location:',ele_user.location)  #{'x': 690, 'y': 46}
print('rect:',ele_user.rect)  #{'height': 23, 'width': 154, 'x': 690.4500122070312, 'y': 46.5}
print(ele_user.get_attribute('id'))  #ls_username

driver.quit()