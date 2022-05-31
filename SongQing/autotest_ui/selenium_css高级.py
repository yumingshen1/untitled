# -*- coding:utf-8 -*-
# @Time : 2022/5/11 22:52
# Auther : shenyuming
# @File : selenium_css高级.py
# @Software : PyCharm
'''
    div p   div下的标签（子孙） //div//p   或者 #div2 p  （div2是div的id的值）
    div>p   div下的p (儿子)     //div/p
    p+input     p标签同级下的input，且紧挨着
    属性：
        [属性=属性值]
    没有函数：
        [属性^=属性值]  开头是。。。
        [属性*=属性值]  包含。。。
        [属性$=属性值]  结尾是。。。

    #div2>input:nth-child(2)    选择属于其父元素(div)下的第二个子元素input
    #lk_content p:last-child   选择属于其父元素(div)下的最后一个元素input

'''
from selenium import webdriver
from time import sleep
import os

with webdriver.Chrome() as driver:
    # file_path = os.path.dirname(__file__)
    # path = os.path.join('file://'+file_path,'test_a.html')
    url = 'http://124.223.31.21:8090/forum.php'
    driver.get(url=url)
    sleep(2)
    #点击登录  弹窗
    driver.find_element_by_css_selector('.pn.vm').click()
    ##变化的ID
    sleep(2)
    driver.find_element_by_css_selector('[id^="username_L"]').send_keys('admin')
    driver.find_element_by_css_selector('.px.p_fre').send_keys('123456')
