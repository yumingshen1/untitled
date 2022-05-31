# -*- coding:utf-8 -*-
# @Time : 2022/5/17 11:40
# Auther : shenyuming
# @File : selenium_css总结.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    url = 'http://124.223.31.21:8090/forum.php'
    driver.get(url=url)
    ##提取论坛底部文本 ,   css的多种找法
    css1 = 'h5+p'
    css2 = '.lk_content.z>p'
    css3 = '#category_lk p'                     #div的id p
    css4 = '#category_lk p:last-child'           #div的id last-child
    css5 = '#category_lk p:nth-child(2)'
    css6 = '[id^="category_l"] p'               ## id 属性方法
    css7 = '[class = "lk_content z"] p'         ## class的属性值要写全
    for i in (css1,css2,css3,css4,css5,css6,css7):
        print(driver.find_element_by_css_selector(i).text)