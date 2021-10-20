import requests

class ApiArticel(object):
    ##收藏
    def api_post_collection(self,url,headers,data):
        ##请求返回结果
       return requests.post(url,headers=headers,json=data)

    ##取消收藏
    def api_delete_collection(self,url,headre):

        return requests.delete(url,headre=headre)
    