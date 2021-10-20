#-*- codeing = utf-8 -*-
#@Time : 2021/7/22 下午5:36
#@Author : yuming shen
#@File : unittest-ddt-文件读取.py
#@Software :PyCharm

from ddt import ddt,data,unpack
import time
import unittest
from selenium import webdriver

'''
提取文件数据到list形式获得数据
'''
#读取文件
def getdata():
    params = []
    file = open('ddt文件读取','r',encoding='utf-8')
    for d in file.readlines():
        params.append(d.strip('\n').split(','))
    return params
def filedata():
    list = []
    filedata = open('ddt文件数据2','r',encoding='utf-8')
    for data in filedata.readlines():
        list.append(data.strip('\n').split(','))
    return list

@ddt
class forTest5(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    # @data(*getdata())
    # @unpack
    # def test_01(self,t,y,u):
    #     print(t)
    #     print(y)
    #     print(u)
    #     print('----')


    @data(*filedata())
    @unpack
    def test_02(self,url,text,input,sub):
        self.driver.get(url)
        self.driver.find_element_by_id(input).send_keys(text)
        self.driver.find_element_by_id(sub).click()


if __name__ == '__main__':
    unittest.main()