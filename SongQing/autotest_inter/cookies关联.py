import requests
import json
host = 'http://120.55.190.222:7080'

##  登录接口，返回cookies
def login(inData):
    url = f'{host}/api/mgr/loginReq'
    pyload = inData
    res = requests.post(url=url,data=pyload)
    return res.cookies

##-------业务接口-----
class Lesson():
    ##初始化方法， 将该类所需的公共的都初始化
    def __init__(self,inCookies):
        self.cookies = inCookies

    ##列出课程
    def list_lesson(self,indata):
        list_url = f'{host}/api/mgr/sq_mgr/'
        list_data = indata
        res = requests.get(url=list_url,params=list_data,cookies=self.cookies)
        #相应编码修改
        res.encoding='unicode_escape'
        return res.text

    ##新增课程
    def add_lesson(self,add_data):
        url = f'{host}/api/mgr/sq_mgr/'
        add_data = add_data
        add_res = requests.post(url=url,data=add_data,cookies=self.cookies)
        return add_res.json()


if __name__ == '__main__':
    cookie = login({'username':'auto','password':'sdfsdfsdf'})
    print('登录返回的cookies---->',cookie)

    list_data = 'action=list_course&pagenum=1&pagesize=20'
    res = Lesson(cookie).list_lesson(list_data)
    print('列表--->',res)


    pyload = {'action':'add_course',
            'data':'{"name":"测试13日","desc":"23分","display_idx":1}'
              }
    print(type(pyload))

    add = Lesson(cookie).add_lesson(pyload)
    print(type(add))
    print('新增的---->',add)