# -*- coding:utf-8 -*-
# @Time : 2022/6/4 20:49
# Auther : shenyuming
# @File : iframe_1.py
# @Software : PyCharm

'''
知识点：iframe切换 ，  driver.swith_to.frame(frame_reference)
frame_reference取值：
    iframe下标：0
    id,name的值 ： #id,name
    webelement对象: driver.find_element_by_css_selector('xxx')
'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep,ctime

with webdriver.Chrome() as driver:
    driver.get(f'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/webdriver_2/test.html')
    test_flage =2

    if test_flage ==1:
        #1，外层写入
        driver.find_element_by_id('uname').send_keys('admin1')
        sleep(2)
        #2，内层写入
        driver.switch_to.frame('nf')    #iframe的name值
        driver.find_element_by_id('username').send_keys('admin2')
        sleep(2)
        #3，外层写入
        driver.switch_to.default_content()      #退出最外层，不在iframe中
        driver.find_element_by_id('uname').clear()
        driver.find_element_by_id('uname').send_keys('admin3')
        sleep(2)
        #4，内层写入
        driver.switch_to.frame(0)       # iframe的下标
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys('admin4')
        sleep(2)
        #5，外层写入
        driver.switch_to.parent_frame()   #向外退出一层iframe,退出当前iframe,如有多层，退出到上一层iframe
        driver.find_element_by_id('uname').clear()
        driver.find_element_by_id('uname').send_keys('admin5')
        sleep(2)
        #6，内层写入
        driver.switch_to.frame(driver.find_element_by_id('if'))  #webelement方式,找到iframe的id
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys('admin6')
        sleep(5)

    ## 稳定切换iframe
    if test_flage ==2:
        mywait = WebDriverWait(driver,5,0.5)
        #定义选择器
        frame_locator = ('id','if')
        # mywait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator)) ##方法1：用选择器
        mywait.until(EC.frame_to_be_available_and_switch_to_it('if'))       # 方法2： 直接输入元素值
        driver.find_element_by_css_selector('#username').clear()
        driver.find_element_by_css_selector('#username').send_keys('11111')

        sleep(3)