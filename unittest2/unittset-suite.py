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
suite、
'''

@ddt
class forTest6(unittest.TestCase):

    def test_01(self,):
        print('1')

    #**kwargs 传入字典形式数据，不知道传入数据量时可以使用
    @file_data('filedata-3.yml')
    def test_02(self,**kwargs):
        name = kwargs.get('name')
        print(name)
        self.assertEqual(name,'unittest',msg='error')
        info = kwargs.get('info')
        print(info)
        self.assertNotEqual(info,'123',msg='相等了')
        print('++++++')

    def test_03(self):
        print('3')

if __name__ == '__main__':
    unittest.main()