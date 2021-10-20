import unittest
from api.api_article import ApiArticel
from parameterized import parameterized
from tools.read_json import ReadJson


##获取数据
def get_data_add():
    data = ReadJson("article_add.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

##获取取消收藏
def get_data_cnacle():
    data = ReadJson("article_cancle.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    return arrs

class TestArticle(unittest.TestCase):

    #收藏方法
    @parameterized.expand(get_data_add())
    def test01_collection(self,url,headers,data,expect_result,status_code):
        ##临时数据
        # url = "http://ttapi/research.itcast.cn/app/v1_0/article/collections"
        # headers = {"Content-Type":"application/json","Authorization":"Bearer token.."}
        # data = {"target":1}

        ##请求
        r = ApiArticel().api_post_collection(url,headers,data)

        print("响应数据：", r.json())

        ##断言
        self.assertEquals(status_code,r.status_code)
        self.assertEquals(expect_result,r.json()['massage'])


    ##取消收藏
    @parameterized.expand(get_data_cnacle())
    def test02_cancle(self,url,headers,status_code):
        ##临时数据
        # url = "http://ttapi/research.itcast.cn/app/v1_0/article/collections/1"
        # headers = {"Content-Type":"application/x-www-from-urlencoded","Authorization":"Bearer token.."}

        d = ApiArticel().api_delete_collection(url,headers)
        ##没有响应数据，d.json()会报错
        print(d.status_code)

        ##断言
        self.assertEquals(status_code, d.status_code)


if __name__ == '__main__':
    unittest.main()
