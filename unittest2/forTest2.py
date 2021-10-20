#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午10:07
#@Author : yuming shen
#@File : forTest2.py
#@Software :PyCharm
import unittest
from selenium import webdriver
import time

class fortestTest(unittest.TestCase):

    def setUp(self) -> None:
        chrome_driver = r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_id('kw').send_keys('测试')
        self.driver.find_element_by_id('su').click()
    def test_02(self):
        self.driver.find_element_by_id('kw').send_keys('unittest')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()