# -*- coding:utf-8 -*-
# @Time : 2022/5/31 22:15
# Auther : shenyuming
# @File : 鼠标操作2_Actionchains.py
# @Software : PyCharm
'''
鼠标移动 悬浮-->点击
move_to_element
move_by_offset
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
sleep(2)
#id元素
ele_menu = driver.find_element_by_css_selector('#qmenu')

test_flag =1
if test_flag ==1:
    print(ele_menu.location)  # x,y
    print(ele_menu.size)    # width, height
    print(ele_menu.rect)  #{'height': 24, 'width': 113, 'x': 1066, 'y': 118}
    x = ele_menu.rect['x']+ele_menu.rect['width']/2 #获得x坐标
    y = ele_menu.rect['y']+ele_menu.rect['height']/2 #获得y坐标
    ActionChains(driver).move_by_offset(x,y).perform()
    sleep(2)
    driver.find_element_by_css_selector('a>strong').click()
    sleep(2)
    driver.quit()

if test_flag ==2:
    ActionChains(driver).move_to_element(ele_menu).perform()  #鼠标移动到目标位置
    sleep(2)
    driver.find_element_by_css_selector('a>strong').click()
    sleep(2)
    driver.quit()
