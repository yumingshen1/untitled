#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午12:35
#@Author : yuming shen
#@File : 线程池爬取梨视频.py
#@Software :PyCharm

import requests
import re
from lxml import etree
from multiprocessing.dummy import Pool

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
url = 'http://www.pearvideo.com/category_5'

page_text = requests.get(url=url,headers=headers).text

#解析
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="listvideo-list clearfix"]/li')
urls = [] #存储所有视频链接和名字
for li in li_list:
    detail_ul = 'http://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    detail_name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    print(detail_name,detail_ul)
    #对详情页地址发请求，解析出视频地址
    detail_page_text = requests.get(url=detail_ul,headers=headers).text
    print(detail_page_text)
    break

    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex,detail_page_text)
    dic = {
        'name':detail_name,
        'url':video_url
    }
    urls.append(dic)

def get_video_data(dic):
    url = dic['url']
    data = requests.get(url=url,headers=headers).content
    with open(dic['name'],'wb') as fp:
        fp.write(data)

pool = Pool(4)
pool.map(get_video_data,urls)

pool.close()
pool.join()