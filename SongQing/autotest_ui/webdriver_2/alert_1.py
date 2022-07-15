# -*- coding:utf-8 -*-
# @Time : 2022/6/4 17:16
# Auther : shenyuming
# @File : alert_1.py
# @Software : PyCharm

'''
知识点：alert
易识别，无法定位元素
alert,confirm,prompt
切换的方法：
accept() : 确定 ---》三个均可用
dismiss(): 取消---> confirm,prompt
send_keys() :输入 ----> prompt
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
driver = webdriver.Chrome()
driver.get(f'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/webdriver_2/test.html')

test_flage = 5

##稳定切换
##问题、面试：点击alert后立即操作accept操作，可能无法及时弹窗，---->等待，显示等待
if test_flage == 5:
    driver.find_element_by_id('alert').click()
    sleep(2)
    alert = WebDriverWait(driver,5,0.5).until(EC.alert_is_present())
    alert.accept()
    sleep(2)
    driver.quit()

##另一种实现
if test_flage == 4:
    driver.find_element_by_id('confirm').click()
    sleep(2)
    Alert(driver).accept()
    sleep(2)
    driver.quit()

#点击prompt输入内容，点击确定
if test_flage == 3:
    driver.find_element_by_id('prompt').click()
    sleep(2)
    driver.switch_to.alert.send_keys('hello! sym')
    sleep(1)
    driver.switch_to.alert.accept()
    sleep(2)
    driver.quit()

#点击confirm按钮 后点击取消
if test_flage ==2:
    driver.find_element_by_id('confirm').click()
    sleep(2)
    driver.switch_to.alert.dismiss()    #取消
    sleep(2)
    driver.quit()

#点击alert按钮后点击确定
if test_flage == 1:
    driver.find_element_by_css_selector('#alert').click()
    sleep(2)
    driver.switch_to.alert.accept()     #确定
    sleep(2)
    driver.quit()