
import requests

##get 带参数
url = 'http://www.baidu.com'
params = {"id":1001}
response = requests.get(url,params=params)
print(response.url)
print(response.status_code)

##get的参数带多个值
paramss = {"id":"1001,1002"}
res = requests.get(url,params=paramss)
print(res.url)
print(res.status_code)
print(res.text)

##多个简直对
paramsss = {"id":1001,"kw":"北京"}
ress = requests.get(url,params=paramsss)
print(ress.url)
print(ress.status_code)
print(ress.text)

print("-------")

response = requests.get("http://wwww.baidu.com")
response.encoding = response.apparent_encoding
print("状态码："+str(response.status_code))
print(response.text)

