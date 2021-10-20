#-*- codeing = utf-8 -*-
#@Time : 2021/8/1 下午6:31
#@Author : yuming shen
#@File : base_page.py
#@Software :PyCharm

from selenium import webdriver
import time

class BasePage:
    #driver = webdriver.Chrome()

    #构造函数,有构造函数才能调用以下方法
    def __init__(self,driver):
        self.driver=driver
    #访问URL
    def visit(self,url):
        self.driver.get(url=url)
    #元素定位，使用元组接受方便管理，一个是元素的方法， 一个是元素的值
    def locator(self,loc):
        return self.driver.find_element(*loc)
    #输入
    def input_(self,loc,text):
        self.locator(loc).send_keys(text)
    #点击
    def click_(self,loc):
        self.locator(loc).click()
    #等待
    def wait(self,time_):
        time.sleep(time_)
    #关闭浏览器
    def quit(self):
        self.driver.quit()