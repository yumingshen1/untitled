# -*- coding:utf-8 -*-
# @Time : 2022/6/3 22:56
# Auther : shenyuming
# @File : 显示等待_5.py
# @Software : PyCharm
'''
最常用的2个方法
visibility_of_element_located ：用于判断特定元素是否存在与DOM树中并且可见，可见意为元素的高和宽大于0元素存在返回元素本身，否咋返回FALSE
presence_of_element_located：用于判断一个元素是否寻在于DOM树中，存在返回元素本身，否则报错
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
ele_username = ('css selector','#ls_username')
ele_passoword = ('css selector','#ls_password')
try:
    WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located(ele_username)).send_keys('admin')
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(ele_passoword)).send_keys('123456')
    print('YES!')
except:
    print('no serch')
sleep(5)
driver.quit()