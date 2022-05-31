# -*- coding:utf-8 -*-
# @Time : 2022/5/31 14:47
# Auther : shenyuming
# @File : 无头浏览器_phantomjs.py
# @Software : PyCharm

'''
selenium4.0 中已删除
配置过程
1. phantomjs-2.1.1-windows.zip
2. 解压，得到一个目录，
3. 把bin目录放到PATH中
4. cmd下输入phantomjs能得到一个如下提示phantomjs>
5. 首次配置重启pycharm
'''
from selenium import webdriver
from time import sleep

driver = webdriver.PhantomJS()  #打开一个无头浏览器
print('名字：',driver.name)
print('尺寸：',driver.get_window_size())
driver.get('http://124.223.31.21:8090/forum.php')
sleep(2)
driver.find_element_by_css_selector('#ls_name').send_keys('dsdsdsd')
sleep(1)
driver.save_screenshot('phantomjs.png')