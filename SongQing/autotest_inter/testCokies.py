
import requests
'''
请求的数据类型 requests.post（）
    1- data  表单 抓包看到的请求体数据格式： a=1&b=2
    2- json  json格式  抓包看到的请求体数据格式  {"a":100}
    3- files  文件接口
    4- params  参数拼接到url  get请求  http://ip:port/路径?a=1&b=3
    
    
    
 -------场景二：cookies需要第三方授权----------------------
"""
自动化脚本怎么实现：
    1- 获取本测试系统的cookies对象的里的sessionID
    2- 编写第三方授权平台的登录接口--认证接口---获取token、uid
    3- 自己组装cookies----- userCookies={‘sessionid’:'xxxxx','token':'xxxxx'}
    4- requests.post(cookies=userCookies)
 
"""
 
'''
host = 'http://120.55.190.222:7080'
def login(indata):
    url = f'{host}/api/mgr/loginReq'
    data = indata
    res = requests.post(url=url,data=data)

    print('请求头----》',res.request.headers)
    print('请求url----》',res.request.url)
    print('请求参数----》', res.request.body)
    print('产生的cookies----》',res.cookies)
    return res.cookies



if __name__ == '__main__':
    r = login({'username':'auto','password':'sdfsdfsdf'})
    print('返回token：',r)