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

    ##将获取的数据放入列表中
    datas = ReadJson("login_more.json").read_json()
    print(datas)

    arrs = []
    ##存在多条用例时，利用字典的values()获取所有值
    for data in datas.values():
        arrs.append((data.get("url"),
                    data.get("mobile"),
                    data.get("code"),
                    data.get("expect_result"),
                    data.get("status_code")))
    print(arrs)
