# -*- coding:utf-8 -*-
# @Time : 2022/6/3 20:22
# Auther : shenyuming
# @File : 显示等待_1.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
显示等待：WebDriverWait ，
expected_conditions：预期条件，是配合WebDriverWait使用
调用方式1：
WebDriverWait(driver,5,0.5).until(条件满足)
调用方式2：
mywait = WebDriverWait(driver,5,0.5)
mywait.until(条件满足)
'''
test_flage = 2

if test_flage ==1:
    with webdriver.Chrome() as driver:
        driver.get('http://121.41.14.39:8088/index.html')
        try:
            ##官方调用方式 lambda 传入的参数:返回值 , x是driver
            WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_css_selector('#username')).send_keys('sq1')
        except:
            print('预期结果不一致')
        sleep(5)

if test_flage ==2:
    with webdriver.Chrome() as driver:
        driver.get('http://121.41.14.39:8088/index.html')
        ##自定义封装
        def my_func(_driver):
            return _driver.find_element_by_css_selector('#username')
        try:
            ##调用封装的
            WebDriverWait(driver,10,0.5).until(my_func).send_keys('sq1')
        except:
            print('预期结果不一致')
        sleep(5)