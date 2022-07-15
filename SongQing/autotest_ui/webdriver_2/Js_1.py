# -*- coding:utf-8 -*-
# @Time : 2022/6/1 19:03
# Auther : shenyuming
# @File : Js_1.py
# @Software : PyCharm
'''
查询需要用到的js的方法，removeAttribute == 方法
removeAttribute site:www.w3school.com.cn

'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://124.223.31.21:8090/forum.php')
test_flage = 6
'''
封装
'''
if test_flage == 6:
    js15 = "arguments[0].value = 'admin'"
    ele_ment = driver.find_element_by_css_selector('#ls_username')
    driver.execute_script(js15,ele_ment)
    sleep(2)
    js16 = "arguments[0].value=arguments[1]"
    #       execute_script(js,参数1=arguments[0],参数2=arguments[1])
    driver.execute_script(js16,ele_ment,'heool')
    sleep(2)
    driver.quit()


'''
css 定位
document.querySelector('#ls_username')  ==== driver.findElement_by_css(#ls_username)
'''
if test_flage == 5:
    js11 = "document.querySelector('#ls_username').value = 'admin'"
    js12 = "document.querySelector('#ls_password').value = '123456'"
    js13 = "document.querySelector('#ls_password').type = 'text'"   #密码的tyoe改为text==明文
    js14 = "document.querySelector('.fastlg_l button').click()"
    driver.execute_script(js11)
    driver.execute_script(js12)
    driver.execute_script(js13)
    driver.execute_script(js14)
    sleep(2)
    driver.quit()
'''
document 定位 
id , classname
document.getElementById('ls_username').value = 'admin'
'''
if test_flage == 4:
    js8 = "document.getElementById('ls_username').value = 'admin'"
    js9 = "document.getElementsByClassName('px')[1].value = '123456'"
    js10 = "document.getElementsByClassName('pn')[0].click()"
    driver.execute_script(js8)
    driver.execute_script(js9)
    driver.execute_script(js10)
    sleep(2)
    driver.quit()

'''
window 滚动条
'''
if test_flage ==3:
    driver.set_window_size(600,800)
    js3 = 'window.scrollTo(0,10000)'
    driver.execute_script(js3)
    sleep(2)
    js4 = 'window.scrollTo(0,0)'
    driver.execute_script(js4)
    sleep(2)
    js5 = 'window.scrollTo(100000,0)'
    driver.execute_script(js5)
    sleep(2)
    js6 = 'window.scrollTo(0,document.body.scrollHeight)'
    js7 = 'window.scrollTo(document.body.scrollWidth,0)'
    driver.execute_script(js6)
    sleep(2)
    driver.execute_script(js7)
    sleep(2)
    driver.quit()

if test_flage ==2:
    js1 = 'return document.title'
    print(driver.execute_script(js1))
    js2 = 'return document.URL'
    print(driver.execute_script(js2))
    sleep(2)
    driver.quit()

if test_flage ==1:
    driver.execute_script("window.open('https://www.baidu.com')")
    sleep(2)
    driver.quit()