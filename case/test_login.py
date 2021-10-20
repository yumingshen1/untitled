'''
登陆业务层
'''
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson
##读取数据函数read
def get_data():
    data = ReadJson("logins.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

#新建测试类,继承unittest才能表示是测试case
class TestLogin(unittest.TestCase):
    #测试方法：
    @parameterized.expand(get_data())   #参数化
    def test_login(self,url,mobile,code,expect_result,status_code):

        ##临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile = "18515607030"
        # code = "548513"

        #调用登陆方法
        s = ApiLogin().api_post_login(url,mobile,code)
        print("响应结果：",s.json())

        ##断言
        self.assertEqual(expect_result,s.json()['message'])
        self.assertEqual(status_code,s.status_code)


if __name__ == '__main__':
    unittest.main()
