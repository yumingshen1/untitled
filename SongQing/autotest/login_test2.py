
import requests
host = 'http://121.41.14.39:8082'           ## 将ip拿出来，为了方便切换环境
password = {"username":"zo0385","password":"c6d1db3b8c9c598d7c810afee405b57c"}
def login2(indata):
    #url = host+路径
    url = f'{host}/account/sLogin'          ## url拼接
    #body
    pylod = indata                          ## 传入参数多一步，为了扩展，例如 加密
    #post
    resp = requests.post(url=url,data=pylod)

    ##打印响应头回头，可看到返回的数据类型
    print(resp.headers)

    return resp.text

if __name__ == '__main__':
    re = login2(password)
    print(re) #TODO ---  MD5