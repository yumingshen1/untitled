#-*- codeing = utf-8 -*-
#@Time : 2021/8/1 下午8:38
#@Author : yuming shen
#@File : test_case_forsearch.py
#@Software :PyCharm

import unittest
import time
from selenium import webdriver
from POM_UNITEST.page_object.login_page import LoginPage
from POM_UNITEST.page_object.index_page import IndexPage
from ddt import ddt,data,file_data,unpack

@ddt
class TestCase(unittest.TestCase):
    #在pom模式中使用setupclass生成一个浏览器更符合页面之间的测试
    @classmethod
    def setUpClass(cls) -> None:
        #初始化需要的页面
        cls.driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
        cls.options = webdriver.ChromeOptions()
        #最大化
        cls.options.add_argument('start-maximized')
        #去掉开发者in警告
        cls.options.add_experimental_option('useAutomationExension',False)

        cls.lg = LoginPage(cls.driver)
        cls.inde = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("hello world")

    @file_data('../data/user.yaml')
    def test_1_login(self,username,password):
        self.lg.login(username, password)
        time.sleep(3)

    @data('电脑','手机')
    def test_2_index(self,txt):
        self.inde.search_(txt)
        time.sleep(3)
