'''
参数化，导入parameterized包

使用：参数化组件
@parameterized.expant(参数)
单个参数用列表
多个参数用列表嵌套元祖
'''

import unittest
from parameterized import parameterized

##新建测试类
class TestPara(unittest.TestCase):
    @parameterized.expand([("admin","123456"),("user02","3356")])
    #新建测试方法
    def test_para(self,username,password):
        print("用户名: ",username)
        print("密码：",password)
