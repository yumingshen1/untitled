
import re
import os
import requests
url = 'http://www.quannovel.com/read/620/'  # 进行爬虫的网址
req = requests.get(url)  # 获取网页的内容
name = re.findall('<h2>(.*?)<i class', req.text)[0]  # 获取书名
mulu = re.findall('class="name ">(.*?)</a>', req.text)
wangzhi = re.findall('<a href="(.*?).html"', req.text)
dict1 = {}
for i in range(len(mulu)):
    dict1[mulu[i]] = f'{url}{wangzhi[i]}.html'  # 将目录和网址放入字典
count = 1

if not os.path.exists(f'/Users/shenyuming/Downloads/sym/tuwen/{name}'):  # 如果没有以书名命名的目录,则新建
    os.mkdir(f'/Users/shenyuming/Downloads/sym/tuwen/{name}')
for k, v in dict1.items():
    if count > 5:
        break
    else:
        req = requests.get(v)  # 获取正文网页的内容
        neirong = re.findall('class="page-content ">(.*?)<div class', req.text, re.S)[0]  # 获取文章内容
        print(neirong)
        neirong = neirong.replace('<p>', '').replace('</p>', '')
        with open(f'/Users/shenyuming/Downloads/sym/tuwen/{name}/{k}.txt', 'w+') as file1:
            file1.write(neirong)
    print(f'第{count}章爬取完毕')
    count += 1