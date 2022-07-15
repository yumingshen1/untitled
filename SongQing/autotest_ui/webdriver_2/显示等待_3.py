# -*- coding:utf-8 -*-
# @Time : 2022/6/3 22:27
# Auther : shenyuming
# @File : 显示等待_3.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
text_to_be_present_in_element   判断某文本是否存在于特定元素value值中
传参    locator 元素的定位器 ，text_  文本
          通过locator定位到一个元素，获取其text
          判断你传入的 text_是否在元素的text中
返回值   True|False
'''
with webdriver.Chrome() as driver:
    driver.get('http://121.41.14.39:8088/index.html')
    try:
        ##定位器
        ele_button_locator = ('css selector','button>span')
        mywait=WebDriverWait(driver,10,0.5)     #轮循等待，最大等待10秒，每0.5秒轮循一次
        mywait.until(EC.text_to_be_present_in_element(ele_button_locator,'登录')) #判断某文本是否存在于特定元素value值中
        print(f'登录在元素{ele_button_locator}中')
    except:
        print(f'登陆不在元素{ele_button_locator}中')
    sleep(5)
    driver.quit()