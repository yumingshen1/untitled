
import requests

##抓包工具的代理地址和端口
find_proixes = {
    'http:':'127.0.0.1:8888',
    'https':'127.0.0.1:8080'
}

def login(data):
    url = 'http://121.41.14.39:8082/account/sLogin'
    payload = data
    resp = requests.post(url=url,data=payload)

    ## 加入proxies=find_proixes 是手动加入代理，让工具能够抓到请求数据， 如果加proxies=find_proixes就一定要开抓包工具，否则报错
    ## resp = requests.post(url=url,params=payload,proxies=find_proixes)

    print(resp.request.url)  ##查看请求url

    print(resp.request.body)    ##查看请求的body

    print(resp.request.headers)  ##查看请求的头

    print(resp.text)




login({"username":"sq0001","password":"1111"})

'''
请求失败，可以用代码抓包
    代码打印对应的请求头、body
    工具抓包，
    代码抓包
'''
