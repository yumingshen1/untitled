#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午9:52
#@Author : yuming shen
#@File : forText.py
#@Software :PyCharm

import unittest

class forTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('类的初始化')
    @classmethod
    def tearDownClass(cls) -> None:
        print('类的释放')

    def setUp(self) -> None:
        print('用例初始化')
    def tearDown(self) -> None:
        print('用例释放')

    def test_01(self):
        print('cehsi 1')
    def test_02(self):
        print('ceshi 2')

if __name__ == '__main__':
    unittest.main(verbosity=2)   #verbosity=2 运行后在下方查看更详细日志
