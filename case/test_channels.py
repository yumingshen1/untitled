import unittest
from api.api_channels import ApiChannels
from parameterized import parameterized
from tools.read_json import ReadJson

##获取数据参数化
def get_data():
    data = ReadJson("channels.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

##测试类
class TestChannels(unittest.TestCase):
    ##测试方法
    @parameterized.expand(get_data())
    def test_chanels(self,url,headers,expect_result,status_code):
        ##临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # headers = {"Content-Type":"application/json","Authorization":"Bearer token,,"}

        ##调用方法
        s = ApiChannels().api_get_channels(url,headers)

        ## 请求返回结果
        print("响应结果：", s.json())

        ##断言
        self.assertEquals(expect_result, s.json()['message'])
        self.assertEquals(status_code, s.status_code)

if __name__ == '__main__':
    unittest.main()
