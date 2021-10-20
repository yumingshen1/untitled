#-*- codeing = utf-8 -*-
#@Time : 2021/8/1 下午7:33
#@Author : yuming shen
#@File : login_page.py
#@Software :PyCharm
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM_UNITEST.base.base_page import BasePage

#继承base包下的base_page的文件下的BasePage类,可以调用此类下的方法
class LoginPage(BasePage):
    #核心元素
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    #base_page的元素定位用的元组接受
    user = (By.NAME,'accounts')
    password = (By.NAME,'pwd')
    login_button = (By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    #核心业务流
    def login(self,username,password):
        self.visit(self.url)
        self.input_(self.user,username)
        self.input_(self.password,password)
        self.click_(self.login_button)



#调试
if __name__ == '__main__':
    driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
    username = 'sym123456'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username,password)
