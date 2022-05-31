# -*- coding:utf-8 -*-
# @Time : 2022/4/11 22:11
# Auther : shenyuming
# @File : selenium_css基础.py
# @Software : PyCharm
'''
    CSS 基础语法
    标签名：#tag_name  如 ： #p 、 #html
    id的值：#id_value 、如： #ls_username
    class的值： .class1.class2
    组合：input#ls_username.px.vm
'''

from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    # file_path = os.path.dirname(__file__)
    # path = os.path.join('file://'+file_path,'test_a.html')
    url = 'http://124.223.31.21:8090/forum.php'
    driver.get(url=url)
    sleep(1)
    driver.find_element_by_css_selector('input#ls_username').send_keys('admin')
    driver.find_element_by_css_selector('#ls_password').send_keys('123456')
    sleep(1)
    driver.find_element_by_css_selector('.pn.vm').click()
    sleep(3)