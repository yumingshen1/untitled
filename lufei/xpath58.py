#-*- codeing = utf-8 -*-
#@Time : 2021/7/10 下午7:46
#@Author : yuming shen
#@File : xpath58.py
#@Software :PyCharm
import requests
from lxml import etree

def main():
    url = "https://bj.58.com/ershoufang/"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    #请求
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    #数据解析
    tree = etree.HTML(page_text)
    #找到每条数据所在的标签
    div_list = tree.xpath('//section[@class="list"]/div')
    # print(div_list)
    fp = open('/Users/shenyuming/Downloads/sym/tuwen/mingzi.txt','w',encoding='utf-8')
    for div in div_list:
        #在每条数据标签的目录下向下找到title的标签，用text()取直系值
        title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
        print(title)
        fp.write(title+'\n')
        print(title+'下载完成！')









if __name__ == '__main__':
    main()