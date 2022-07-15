# -*- coding:utf-8 -*-
# @Time : 2022/6/5 15:41
# Auther : shenyuming
# @File : 文件上传.py
# @Software : PyCharm
'''
文件上传：
input 标签的直接send_keys
非input 标签的---第三方库
    pyautohui
    pywinauto
    pywin32
'''

from selenium import webdriver
from time import sleep
import pyautogui
driver = webdriver.Chrome()
driver.get('http://121.41.14.39:8088/index.html#/')
driver.find_element_by_id('username').send_keys('sq1')
driver.find_element_by_id('password').send_keys('123')
driver.find_element_by_id('code').send_keys('999999')
driver.find_element_by_id('submitButton').click()
driver.refresh()
sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'文件上传')]").click()
sleep(2)
test_flage =2

if test_flage ==2:  ##单文件上传 非input
    driver.find_element_by_xpath("//li[contains(text(),'非input')]").click()
    sleep(1)
    driver.find_element_by_css_selector('.el-icon-upload').click()
    sleep(1)
    pyautogui.typewrite(r'/Users/shenyuming/Downloads/新建文本文档.txt')
    pyautogui.press('enter')
    sleep(2)

if test_flage ==1: ##单文件上传，input
    driver.find_element_by_xpath("//li[contains(text(),'单文件上传')]").click()
    sleep(2)
    driver.find_element_by_css_selector('#cover').send_keys(r'/Users/shenyuming/Downloads/55期课程表.png')
    sleep(2)

driver.quit()