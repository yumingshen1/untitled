'''
登陆接口
'''
#导包
import requests
import json
#新建类，登陆接口对象
class ApiLogin(object):
    #新建方法，登陆
    def api_post_login(self,url,mobile,code):
        #headers
        headers = {"Content-Type":"application/json"}
        #data
        data = {"moble":mobile,"code":code}
        #调用并返回响应
        return requests.post(url,headers=headers,json=data)
