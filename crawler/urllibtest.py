#-*- codeing = utf-8 -*-

import urllib.request,urllib.parse
#获取get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码


#获取post请求    httpbin.org 请求和相应的网站

#post方式参数必须转为字节bytes类型传递
# data = bytes(urllib.parse.urlencode({"hellow":"word","w":"a"}),encoding ="utf-8")
# response = urllib.request.urlopen('http://httpbin.org/post',data = data)
# print(response.read().decode("utf-8"))

#超时处理
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


#处理识别爬虫
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'terci'}).encode('utf-8'))
# #封装一个请求对象
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# #解析封装的请求对象
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


###访问豆瓣网 get
url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
#封装一个请求对象
req = urllib.request.Request(url=url,headers=headers)
#解析封装的请求对象
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

