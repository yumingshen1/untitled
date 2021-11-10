
import requests
import hashlib
from urllib import parse

## md5加密
def MD5_login(**kwargs):
    dict1 = dict(sorted(kwargs.items(),key=lambda item:item[0]))    ##对请求参数做asci11的排序处理
    datas = parse.urlencode(dict1)              ## 对请求参数做urlencode编码
    pwd = hashlib.md5()                     ## MD5加密
    pwd.update(datas.encode(encoding='utf-8'))
    return pwd.hexdigest()

##测试环境地址
host = 'http://121.41.14.39:8082'
# pwd = "44982"
# data = {"username":"zo0385","password":MD5_login(pwd)}
data = MD5_login(username="zo0385",password="44982")

def login_url(Indata):
    ##url
    url =f'{host}/account/sLogin'
    ##data
    pyload = Indata
    ##request
    res = requests.post(url=url,data=pyload)
    print(res.request.url)
    print(res.request.headers)
    print(res.request.body)
    print(res.text)
    print(res.json())

if __name__ == '__main__':
    login_url(data)