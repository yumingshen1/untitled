# -*- coding:utf-8 -*-
# @Time : 2022/5/18 11:57
# Auther : shenyuming
# @File : selenium_元素上定位元素.py
# @Software : PyCharm

from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('http://124.223.31.21:8090/forum.php')
    ele_login = driver.find_element_by_css_selector('.pn.vm')   ## css定位 calss
    ## 通过登录按钮buttonb标签的class的属性值， 去定位button里面的 em标签的内容
    name = ele_login.find_element_by_tag_name('em').text
    print(name)
