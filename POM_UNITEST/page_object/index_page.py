#-*- codeing = utf-8 -*-
#@Time : 2021/8/1 下午9:04
#@Author : yuming shen
#@File : index_page.py
#@Software :PyCharm


#继承base包下的base_page的文件下的BasePage类
from selenium import webdriver
from selenium.webdriver.common.by import By

from POM_UNITEST.base.base_page import BasePage


class IndexPage(BasePage):
    #核心元素
    url = 'http://39.98.138.157/shopxo/'
    search_input = (By.NAME,'wd')
    earch_button = (By.ID,'ai-topsearch')

    #核心业务流
    def search_(self,text):
        self.visit(self.url)
        self.input_(self.search_input,text)
        self.click_(self.earch_button)

if __name__ == '__main__':
    driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
    txt = '手机'
    inde = IndexPage(driver)
    inde.search_(txt)