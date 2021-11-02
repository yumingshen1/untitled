import re
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'http://www.quannovel.com/read/620'
req = requests.get(url)
name = re.findall('<h2>(.*?)<i class=',req.text)[0]  ##获取书名
mulu = re.findall('class="name ">(.*?)</a>',req.text) ##获取目录
wangzhi = re.findall('<a href="(.*?).html" title=',req.text) ##获取网址
# print(mulu,wangzhi)

dict1 = {}
for i in range(len(mulu)):
    dict1[mulu[i]]=f'{url}{wangzhi[i]}.html'

count = 1
###如果该目录不存在就创建，
if not os.path.exists(f'/Users/shenyuming/Downloads/sym/tuwen/{name}'):
    os.mkdir(f'/Users/shenyuming/Downloads/sym/tuwen/{name}')

for k ,v in dict1.items():
    if count > 5:
        break
    else:
        req = requests.get(v)
        couent = re.findall('class="page-content ">(.*?)<div class=',req.text,re.S)[0]
        print(type(couent))