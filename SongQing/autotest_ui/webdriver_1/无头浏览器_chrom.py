# -*- coding:utf-8 -*-
# @Time : 2022/5/31 15:05
# Auther : shenyuming
# @File : 无头浏览器_chrom.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep

## 实例化chromoption
options = webdriver.ChromeOptions()
# 设置启动参数---无头运行
options.add_argument('--headless')
## 参数传入浏览器
driver = webdriver.Chrome(options=options)
print('浏览器名字：',driver.name)
print('尺寸大小:',driver.get_window_size())
driver.get('http://124.223.31.21:8090/forum.php')
driver.find_element_by_css_selector('#ls_username').send_keys('admin')
driver.save_screenshot('chromeoptions.png') #截图
sleep(1)
driver.quit()
