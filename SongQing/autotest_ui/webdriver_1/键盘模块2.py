# -*- coding:utf-8 -*-
# @Time : 2022/5/31 18:12
# Auther : shenyuming
# @File : 键盘模块2.py
# @Software : PyCharm
'''
知识点：点击操作|拖拽|按住松开|发送到元素的按键
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/')
test_flag = 1
'''
send_keys_to_element   发送某个键到指定元素
'''
if test_flag ==1:
    driver.get('http://124.223.31.21:8090/forum.php')
    sleep(2)
    username = driver.find_element_by_css_selector('#ls_username')
    passwprd = driver.find_element_by_css_selector('#ls_password')
    ActionChains(driver).send_keys_to_element(username,'admin').send_keys_to_element(passwprd,'123456').perform()
    sleep(2)
    driver.quit()

'''
拖动 drag_and_drop 的源码实现--分别点击拖动元素和目标元素
'''
if test_flag ==4:
    driver.find_element_by_link_text('Drag Drop Test').click()
    sleep(1)
    #获得外层的拖动元素element
    ele_drag = driver.find_element_by_css_selector('#dragger')
    #获得目标元素集
    ele_drop_items = driver.find_elements_by_css_selector('item')
    for ele_drop_item in ele_drop_items:
        myAction = ActionChains(driver)
        myAction.click_and_hold(ele_drag)   #点击拖动元素，不松手
        myAction.release(ele_drop_item) #拖到目标元素
        myAction.perform()  #执行
        sleep(1)
    driver.quit()

'''
拖动 drag_and_drop（位置1，位置2）
'''
if test_flag ==3:
    driver.find_element_by_link_text('Drag Drop Test').click()
    sleep(1)
    #获得外层拖动的的element元素
    ele_drag = driver.find_element_by_css_selector('#dragger')
    #获得目标元素集
    ele_drop_items = driver.find_elements_by_css_selector('.item')
    for ele_drop_item in ele_drop_items:
        ActionChains(driver).drag_and_drop(ele_drag,ele_drop_item).perform()
        sleep(1)
    driver.quit()

'''
单击，双击， 右键
'''
if test_flag ==2:
    driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(5) > a:nth-child(1)').click()
    sleep(2)
    #先找到元素
    ele_click = driver.find_element_by_css_selector("input[value='click me']")
    ele_douclick = driver.find_element_by_css_selector("input[value='dbl click me']")
    ele_rightclick = driver.find_element_by_css_selector("input[value='right click me']")

    ActionChains(driver).click(ele_click).perform()     #单击
    ActionChains(driver).double_click(ele_douclick).perform()   #双击
    ActionChains(driver).context_click(ele_rightclick).perform()    #右键

    sleep(2)
    driver.quit()