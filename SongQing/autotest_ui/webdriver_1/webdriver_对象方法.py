# -*- coding:utf-8 -*-
# @Time : 2022/5/30 14:56
# Auther : shenyuming
# @File : webdriver_对象方法.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
with webdriver.Chrome() as driver:
    path1 = 'http://121.41.14.39:8088/index.html#/'
    path2 = 'http://124.223.31.21:8090/forum.php'

    test_flage = 1
    if test_flage ==1:
        driver.get(path2)
        sleep(2)
        driver.find_element_by_css_selector('#ls_username').send_keys('ad') #用户名
        driver.find_element_by_link_text('立即注册').click()  #登录
        sleep(2)
        driver.back()       #返回
        driver.find_element_by_css_selector('.px.vm').send_keys('min')  #用户名
        sleep(2)
        driver.forward()        #前进
        sleep(2)

    if test_flage == 4:
        driver.get(path1)
        sleep(2)
        driver.minimize_window() #最小化
        sleep(2)
        driver.fullscreen_window() #全屏
        sleep(2)
        driver.maximize_window() #最大化
        sleep(2)
        driver.set_window_size('900','600')  #宽 高
        sleep(2)
        driver.set_window_position('200','300') #X,Y
        sleep(2)
        driver.set_window_rect(300,300,300,300)

    if test_flage == 3:
        driver.get(path1)
        sleep(2)
        print('页面title:',driver.title)
        print('浏览器name:',driver.name)
        print('访问url:',driver.current_url)
        print('窗口大小:',driver.get_window_size())
        print('宽高和坐标rect:',driver.get_window_rect())
        print('坐标position:',driver.get_window_position())
        driver.save_screenshot('driver截图.png') ## driver直接截图
        print('*'*20)
        print('源码：',driver.page_source)

    if test_flage == 2:
        driver.get(path1)
        sleep(2)
        driver.quit()       #关闭chromedriver进程
        # driver.close()      #关闭当前tab页面，一般用于多个tab页面时 , 不关闭chromedriver进程
