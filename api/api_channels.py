import requests

##新建对象类
class ApiChannels(object):
    #新建获取用户频道列表方法
    def api_get_channels(self,url,headers):
        #请求get  返回结果
       return requests.get(url,headers=headers)
