#-*- codeing = utf-8 -*-
#@Time : 2021/7/19 下午2:50
#@Author : yuming shen
#@File : 无头浏览器和规避操作.py
#@Software :PyCharm

from selenium import  webdriver
from selenium.webdriver import ActionChains
from time import sleep
#无头浏览器
from selenium.webdriver.chrome.options import Options
#规避检测识别
from selenium.webdriver import ChromeOptions


# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

#实例化浏览器对象，将无头浏览器对象和规避检测对象传入
bro = webdriver.Chrome(executable_path='/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver',chrome_options=chrome_options,options=option)

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
print(bro.page_source)