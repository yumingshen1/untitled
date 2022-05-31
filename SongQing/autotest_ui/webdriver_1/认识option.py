# -*- coding:utf-8 -*-
# @Time : 2022/5/31 15:31
# Auther : shenyuming
# @File : 认识option.py
# @Software : PyCharm
'''
知识点:  其他option
--incognito

'''
from selenium import webdriver
from time import sleep

test_flage =1
if test_flage ==1:
    option = webdriver.ChromeOptions()
    ##获得浏览器用户数据 ,浏览器输入：chrome://version 选择个人资料路径        有一定的成功率 （Default 去掉）
    user_data_url = '/Users/shenyuming/Library/Application Support/Google/Chrome/Default'
    option.add_argument(f'--user-data-dir={user_data_url}')
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.baidu.com')
    sleep(2)
    driver.quit()

if test_flage ==2:
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')  #无痕参数
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.jianshu.com/p/04848a35fe0a')
    sleep(2)
    driver.quit()