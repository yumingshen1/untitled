# -*- coding:utf-8 -*-
# @Time : 2022/3/17 21:20
# Auther : shenyuming
# @File : one_selenium.py
# @Software : PyCharm

from selenium import webdriver
from pathlib import Path
from time import sleep
import os

'''
    浏览器启动方式 和 获得driver的对象方法和属性
'''

driver = webdriver.Chrome()

# 绝对路径打开本地文件 , 输入绝对路径
# driver.get(r'file:///Users/shenyuming/PycharmProjects/untitled/SongQing/autotest_ui/test_a.html')
# sleep(3)
# driver.quit()


# pathlib打开本地文件
# html_path = str(Path('test_a.html').resolve())
# html_p = '%s'%('file://')+html_path
# driver.get(html_p)
# sleep(2)
# driver.quit()


# os 打开本地文件
# path = os.path.dirname(__file__)
# pt = os.path.join('{}'.format('file://')+path,'test_a.html')
# driver.get(pt)
# sleep(2)
# driver.quit()

# 优雅的打开浏览器
# with webdriver.Chrome() as driver:
#     driver.get('https://www.baidu.com')
#     sleep(1)
#     driver.find_element('id','kw').send_keys('飞机')
#     driver.find_element('id','su').click()
#     sleep(2)


path = os.path.dirname(__file__)  # 打印文件所在目录
path2 = os.path.abspath(__file__) # 打印文件的绝对路径
print(path)
print(path2)


'''
    webdriver的对象方法和属性 , 不看 _开头的方法
'''
test_flage =2
if test_flage == 1:
    for _ in dir(driver):
        if _[0] != '_':
            print(_)

if test_flage == 2:
    for _ in dir(driver):
        if _[:4] == 'find':
            print(_)



