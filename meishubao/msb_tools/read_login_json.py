import json

# #读取json文件的数据  ,推断一
# with open("../msb_data/msb_login.json","r",encoding="utf-8") as f:
#     #loads加载文件流
#     data = json.load(f)
#     print(data)


# 使用函数封装  ,推断二
# def read_json():
#     # 读取json文件的数据
#     with open("../msb_data/msb_login.json", "r", encoding="utf-8") as f:
#         # loads加载文件流
#         data = json.load(f)
#         print(data)


#参数替换文件，
class ReadJson(object):
    #初始化函数，获取文件路径名称
    def __init__(self,filename):
        self.filpath = "../msb_data/"+filename
    #读取数据函数
    def read_json(self):
        # 读取json文件的数据，打开文件流
        with open(self.filpath, "r", encoding="utf-8") as f:
            # loads加载文件流
            data = json.load(f)
            #print(data)
        return data

if __name__ == '__main__':
    # ReadJson("msb_login.json").read_json()

    data = ReadJson("msb_login.json").read_json()
    #新建空列表，添加读取的json数据，将字典格式变为列表套元祖
    arrs = []
    #使用get取值因为如果key输入是错误的结果会直接返回null，不会报错
    arrs.append((data.get("url"),
                 data.get("username"),
                 data.get("password"),
                 data.get("width"),
                 data.get("login"),
                 data.get("ret")))
    print(arrs)
