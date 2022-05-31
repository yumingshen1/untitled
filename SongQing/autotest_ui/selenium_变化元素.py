# -*- coding:utf-8 -*-
# @Time : 2022/5/17 15:46
# Auther : shenyuming
# @File : selenium_变化元素.py
# @Software : PyCharm
'''
http://121.41.14.39:8088/index.html#/home   ui平台先点击输入框再点击单行输入框
'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    url = ' http://121.41.14.39:8088/index.html#/'
    driver.get(url)
    sleep(2)
    driver.find_element_by_css_selector('input#username').send_keys('sq12')
    driver.find_element_by_css_selector('input#password').send_keys('123')
    driver.find_element_by_css_selector('input#code').send_keys('999999')
    driver.find_element_by_css_selector('.el-button.el-button--primary.el-button--normal').click()
    sleep(2)
    ## 刷新浏览器
    driver.refresh()
    sleep(1)
    driver.find_element_by_css_selector('.el-submenu__title').click()
    sleep(1)

    ## 点击 单行输入框会报错，是变化的， TODO   .is-active动态属性值
    # driver.find_element_by_css_selector('.el-menu-item.is-active').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[1]').click()