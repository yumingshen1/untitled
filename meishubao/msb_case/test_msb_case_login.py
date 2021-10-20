import requests
import unittest
from meishubao.msb_api.mab_inte_api import APIrequest
from parameterized import parameterized  #参数化
from meishubao.msb_tools.read_login_json import ReadJson  #导入提取数据类


#提取数据
def get_data():
    data = ReadJson("msb_login.json").read_json()
    # 新建空列表，添加读取的json数据，将字典格式变为列表套元祖
    arrs = []
    # 使用get取值因为如果key输入是错误的结果会直接返回null，不会报错
    arrs.append((data.get("url"),
                 data.get("username"),
                 data.get("password"),
                 data.get("width"),
                 data.get("login"),
                 data.get("ret")))
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def testlogin(self,url,username,password,width,login,ret):

        #调用登录方法
        res = APIrequest().msb_api_login(url,username,password,width)
        #将unicode编码进行解码
        res.content.decode(encoding="utf-8")
        print(res.json())

        #断言
        self.assertEqual(login,res.json()['login'])
        self.assertEqual(ret,res.json()['ret'])
        self.assertEqual(200,res.status_code)

if __name__ == '__main__':
    unittest.main()



