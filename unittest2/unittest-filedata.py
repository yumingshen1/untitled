#-*- codeing = utf-8 -*-
#@Time : 2021/7/22 下午5:36
#@Author : yuming shen
#@File : unittest-ddt-文件读取.py
#@Software :PyCharm

from ddt import ddt,data,unpack,file_data
import time
import unittest
from selenium import webdriver
import yaml

'''
filedata文件形式读取数据
'''

@ddt
class forTest6(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
    # def tearDown(self) -> None:
    #     time.sleep(3)
    #     self.driver.quit()


    # @file_data('filedata.yml')
    # def test_01(self,text):
    #     print(text)

    #
    # @file_data('filedata的格式.yml')
    # def test_01(self, text):
    #     print(text)

    #**kwargs 传入字典形式数据，不知道传入数据量时可以使用
    @file_data('filedata-3.yml')
    def test_02(self,**kwargs):
        name = kwargs.get('name')
        print(name)
        self.assertEqual(name,'unittest',msg='error')
        info = kwargs.get('info')
        print(info)
        self.assertNotEqual(info,123,msg='相等了')
        print('++++++')


if __name__ == '__main__':
    unittest.main()