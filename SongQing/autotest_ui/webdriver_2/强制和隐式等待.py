# -*- coding:utf-8 -*-
# @Time : 2022/6/3 17:01
# Auther : shenyuming
# @File : 强制和隐式等待.py
# @Software : PyCharm

'''
强制： sleep  #固定的等待 #from time import sleep
             #不稳定: 网络波动、机器性能会导致元素加载的时间不可控
             #用于演示，观察效果
             #但是特殊的情况下反而要用sleep
隐式：
driver.implicitly_wait(10)  隐式等待,打开浏览器后就设置时间，应用于全局，即便找的元素提前出来，仍然会等待到设置的时间后才会执行 ， 浪费时间
'''

from selenium import webdriver
from time import sleep,ctime
import ddddocr

with webdriver.Chrome() as driver:
    driver.implicitly_wait(20)      # 隐式等待，
    driver.get('http://124.223.31.21:8090/forum.php')
    try:
        print(ctime())  # js修改元素:document.getElementsByName('username')[0].id = 'ls_usernam' 在规定时间内找到元素才会执行
        driver.find_element_by_css_selector('#ls_usernam').send_keys('admin123')
    except:
        print(ctime())
        print('元素没找到')
    finally:
        print(ctime())
        sleep(5)
        driver.quit()