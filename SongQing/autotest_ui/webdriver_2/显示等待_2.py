# -*- coding:utf-8 -*-
# @Time : 2022/6/3 22:00
# Auther : shenyuming
# @File : 显示等待_2.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.support.wait import WebDriverWait
'''
轮循查找：
修untill改源代码：添加78，79行两行代码，  记得修改后要改回去
              time.sleep(self._poll)
          78  from time import ctime
          79  print(f'我等了{self._poll}秒',ctime())
              if time.time() > end_time:
                  break
'''
with webdriver.Chrome() as driver:
    driver.get('http://121.41.14.39:8088/index.html')
    try:
        print(ctime()) #通过js修改属性值 ele = document.getElementById('username') , ele.id = 'usernam'
        WebDriverWait(driver,20,0.5).until(lambda x:x.find_element_by_css_selector('#usernam')).send_keys('admin')
    except:
        print(ctime())
        print('没有找到')

    print(ctime())
    sleep(5)
    driver.quit()