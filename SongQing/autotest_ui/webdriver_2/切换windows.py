# -*- coding:utf-8 -*-
# @Time : 2022/6/5 12:39
# Auther : shenyuming
# @File : 切换windows.py
# @Software : PyCharm

'''
知识点：window
利用 window handles切换
稳定切换 显示等待
    webdriverwait , excepted_conditions-->new_windowed_is_opened ,  number_of_windows_to_be
'''

from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as driver:
    print('默认当前窗口：',driver.current_window_handle)
    print('获得当前窗口数量：',driver.window_handles)
    olds_window = driver.window_handles
    driver.get(f'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/webdriver_2/test.html')
    print('打开地址后的当前窗口：',driver.current_window_handle)
    print('打开地址后的窗口数量：',driver.window_handles)
    ##点击链接，打开新的窗口
    driver.find_element_by_link_text('百度一下').click()
    print('打开百度连接后窗口数量：',driver.window_handles)

    test_flage =3
    if test_flage ==1:
        #切换到新的窗口
        driver.switch_to.window(driver.window_handles[-1])

    ## 稳定切换 方法1--- webdriverwwait --- excepted_conditions
    if test_flage ==2:
        mywait = WebDriverWait(driver,10,0.5)
        if mywait.until(EC.new_window_is_opened(olds_window)):
            driver.switch_to.window(driver.window_handles[-1])

    ## 稳定切换 方法2
    if test_flage ==3:
        mywait = WebDriverWait(driver,5,0.5)
        if mywait.until(EC.number_of_windows_to_be(len(olds_window)+1)):
            driver.switch_to.window(driver.window_handles[-1])

    ## TODO 切换回之前的窗口，   新打开的窗口不是最后一个

    driver.find_element_by_id('kw').send_keys('UI')
    driver.find_element_by_id('su').click
    sleep(3)
    driver.quit()