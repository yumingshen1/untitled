# -*- coding:utf-8 -*-
# @Time : 2022/5/18 11:16
# Auther : shenyuming
# @File : selenium_find_element.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    url =  'http://124.223.31.21:8090/forum.php'
    driver.get(url)
    sleep(2)
    driver.find_element_by_id('ls_username').send_keys('a')
    driver.find_element(By.ID,'ls_username').send_keys('d')
    driver.find_element('id','ls_username').send_keys('m')
    ele_username_locator1 = ('id','ls_username')        ## 定义好id和id的元素
    driver.find_element(*ele_username_locator1).send_keys('i') ## 调用时元组需要解包 *
    ele_username_locator2 = ['id','ls_username']
    driver.find_element(*ele_username_locator2).send_keys('n')
    ele_username_locator3 = 'id','ls_username'          ## 该方法也是元组
    driver.find_element(*ele_username_locator3).send_keys('x')
    sleep(2)