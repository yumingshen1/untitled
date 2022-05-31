# -*- coding:utf-8 -*-
# @Time : 2022/5/31 15:18
# Auther : shenyuming
# @File : 无头浏览器_firefox.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get('http://124.223.31.21:8090/forum.php')
print('浏览器名字：',driver.name)
print('尺寸大小：',driver.get_window_size())
sleep(2)
driver.find_element_by_xpath('//*[@id="ls_username"]').send_keys('dsds')
driver.save_screenshot('firefoxoptions.png')
sleep(2)
driver.quit()
