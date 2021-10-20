#-*- codeing = utf-8 -*-
#@Time : 2021/6/27 下午6:50
#@Author : yuming shen
#@File : Pic_request.py
#@Software :PyCharm
import requests
import re
import os
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import time

def main():
    url = 'http://www.ejsedu.com/lzss/97264.html'
    # ask(url)
    get_pic(url)

#正则
findpic =re.compile(r'<img alt="励志图片2021新图片头像" src="(.*?)">')


def get_pic(url):
    html = ask(url)
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for item in soup.find_all('div', class_="entry-content"):
        item = str(item)
        pic = re.findall(findpic, item)
        print(pic)
        if len(pic) !=0:
            #将每个地址取出存放单独的list
            for k in range(len(pic)):
                picTmp = pic[k].replace('"/></p><p align="center'," ")
                print(picTmp)
                file_name = picTmp.split('/')[-1]
                print(file_name)
                urllib.request.urlretrieve(picTmp,'/Users/shenyuming/Downloads/sym/tuwen/ejsedu/'+file_name+'.jpg')


def ask(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.114Safari / 537.36"
    }
    request = urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.HTTPError as h:
        print(h.code,h.reason,h.headers,sep='\n')
    except urllib.error.URLError as u:
        print(u.reason)
    return html




if __name__ == '__main__':
   main()