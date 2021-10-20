#-*- codeing = utf-8 -*-
#@Time : 2021/7/19 下午12:07
#@Author : yuming shen
#@File : selenium基础用法.py
#@Software :PyCharm

from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
bro.get('https://www.tmall.hk/')
sleep(1)
#标签定位
select_s = bro.find_element_by_name('q')
select_s.send_keys('护肤品')
btn = bro.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button')
sleep(2)
#执行js代码，滚动一屏
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
btn.click()
sleep(3)

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()

sleep(5)
bro.quit()


