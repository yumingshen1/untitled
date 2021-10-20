import json

#封装读取文件
class ReadJson(object):
    def __init__(self,filename):
        ##获取文件路径
        self.filepath = "../data/"+filename

    def read_json(self):
        ##打开json文件并获取文件流
        with open(self.filepath,"r",encoding="utf-8") as f:
            ##调用load方法加载文件流
            # data = json.load(f)
            # print(data)
            return json.load(f)

if __name__ == '__main__':
    #print(ReadJson("login.json").read_json())

    ## 登陆测试数据   将获取的数据放入列表中
    data = ReadJson("logins.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)


    #
    # ##频道列表测试数据
    # data = ReadJson("channels.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)
    #
    #
    # ##获取收藏
    # data = ReadJson("article_add.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("data"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)
    #
    #
    #
    # ##取消收藏
    # data = ReadJson("article_cancle.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("status_code")))
    # print(arrs)
