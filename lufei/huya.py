#-*- codeing = utf-8 -*-
#@Time : 2021/6/27 下午8:44
#@Author : yuming shen
#@File : huya.py
#@Software :PyCharm

from urllib.request import urlretrieve  #通过图片地址下载图片
import requests
from lxml import etree              #数据预处理
import time

def huya_spider():
    url = 'https://www.huya.com/g/4079'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    respone = requests.get(url=url,headers=headers)
    data = etree.HTML(respone.text)
    frends_list = data.xpath('//img[@class="pic"]')
    for image in frends_list:
        img = image.xpath('./@data-original')[0]
        img = img.split('?')[0]
        name = image.xpath('./@alt')[0]
        urlretrieve(img,'/Users/shenyuming/Downloads/sym/tuwen/huya/'+name+'.jpg')
        print('%s下载完成'%name)
        time.sleep(1)

# urlretrieve('https://anchorpost.msstatic.com/cdnimage/anchorpost/1040/eb/2b5acc5627cf06fd2e15ffb43cbb15_4079_1623231007.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp','a.jpg')


if __name__ == '__main__':
    huya_spider()