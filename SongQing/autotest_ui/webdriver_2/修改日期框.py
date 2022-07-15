# -*- coding:utf-8 -*-
# @Time : 2022/6/2 21:36
# Auther : shenyuming
# @File : 修改日期框.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
import ddddocr

with webdriver.Chrome() as driver:
    driver.get('http://121.41.14.39:8088/index.html#/')
    sleep(2)
    driver.find_element_by_css_selector('#username').send_keys('sq1')
    sleep(1)
    driver.find_element_by_css_selector('#password').send_keys('123')
    sleep(1)
    img = driver.find_element_by_css_selector('img')    #获得图片的tab
    ocr = ddddocr.DdddOcr()         #实例化ocr
    text = ocr.classification(img.screenshot_as_png) #获得图片内容
    driver.find_element_by_css_selector('.el-input__inner.fm-text.itxt-error.dlcode').send_keys(text)
    sleep(1)
    driver.find_element_by_css_selector('#submitButton').click()
    sleep(2)
    driver.refresh()
    driver.find_element_by_css_selector('ul>li:nth-child(3)>div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[3]/ul/li[1]').click()
    sleep(1)
    ##操作转正时间输入框
    js = "document.getElementById('conversionTime').removeAttribute('readonly')"
    js2 = "ele_time = document.getElementById('conversionTime');ele_time.readOnly = false"
    driver.execute_script(js)
    driver.find_element_by_css_selector('#conversionTime').clear()
    driver.find_element_by_css_selector('#conversionTime').send_keys('2020-01-01')
    sleep(2)
    print('wancheng')

