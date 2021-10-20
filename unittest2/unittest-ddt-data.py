#-*- codeing = utf-8 -*-
#@Time : 2021/7/22 下午4:55
#@Author : yuming shen
#@File : unittest-ddt-data.py
#@Software :PyCharm
from selenium import webdriver
from ddt import ddt,data,unpack,file_data
import time
import unittest

'''
直接传入参数
'''

@ddt
class fortest3(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('开始')
    #     self.driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
    #     self.driver.get('http://www.baidu.com')

    # def tearDown(self) -> None:
    #     time.sleep(5)
    #     self.driver.quit()
    #     print('结束')

    #单个参数
    # @data('测试','unittest')
    # def test_A(self,text):
    #     self.driver.find_element_by_id('kw').send_keys(text)
    #     self.driver.find_element_by_id('su').click()

    #多个参数
    @data(('测试','练习'),('unittest','pytest'))
    @unpack
    def test_B(self,text,test):
        print(text)
        print(test)
        print('---')


if __name__ == '__main__':
    unittest.main()