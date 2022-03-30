# -*- coding:utf-8 -*-
# @Time : 2022/3/30 21:22
# Auther : shenyuming
# @File : selenium_login.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep

with webdriver.Chrome() as driver:
    driver.get('http://120.55.190.222:38090/#/login')
    sleep(2)
    driver.find_element_by_name('username').send_keys('鸿星尔克286')
    driver.find_element_by_name('password').send_keys('123456')
    driver.find_element_by_class_name('el-button').click()
    sleep(3)