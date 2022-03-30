# -*- coding:utf-8 -*-
# @Time : 2022/3/30 21:34
# Auther : shenyuming
# @File : selenium_xpath路径法.py
# @Software : PyCharm

'''
    xpath 路径法
'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join('{}'.format('file://')+file_path,'text_b.html')
    driver.get(path)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[1]/input[1]').click()
    # sleep(2)
    # driver.find_element_by_xpath('//div[2]/input[1]').click()
    sleep(2)