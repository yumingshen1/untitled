
import requests
import hashlib
import copy

## md5加密
def MD5_login(str):
    pwd = hashlib.md5()
    pwd.update(str.encode(encoding='utf-8'))
    return pwd.hexdigest()

##测试环境地址
host = 'http://121.41.14.39:8082'
data = {"username":"zo0385","password":"44982"}
def login_url(Indata):
    ##url
    url =f'{host}/account/sLogin'
    ##data
    ## 一层的数据，先浅拷贝一下，防止之后在使用该数据的时候已经是被加密的
    Indata = copy.copy(Indata)
    ## 将字典的password用键改下值，调用封装的md5，就是加密
    Indata['password'] = MD5_login(Indata['password'])
    pyload = Indata
    print(pyload)
    ##request
    res = requests.post(url=url,data=pyload)
    print(res.request.url)
    print(res.request.headers)
    print(res.request.body)
    print(res.text)
    print(res.json())

if __name__ == '__main__':
    login_url(data)