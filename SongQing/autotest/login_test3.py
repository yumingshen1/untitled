
import requests
import hashlib

## md5加密
def MD5_login(str):
    pwd = hashlib.md5()
    pwd.update(str.encode(encoding='utf-8'))
    return pwd.hexdigest()

##测试环境地址
host = 'http://121.41.14.39:8082'
pwd = "44982"
data = {"username":"zo0385","password":MD5_login(pwd)}
def login_url(Indata):
    ##url
    url =f'{host}/account/sLogin'
    ##data
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