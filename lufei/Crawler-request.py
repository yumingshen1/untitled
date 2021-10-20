#-*- codeing = utf-8 -*-
#@Time : 2021/6/25 下午4:04
#@Author : yuming shen
#@File : Crawler-request.py
#@Software :PyCharm

import requests
import json

def main():
    head={
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.114Safari / 537.36"
    }
    # url = "https://www.sogou.com/web"
    # kw = input('请输入：')
    # param = {
    #     'query':kw
    # }
    # respone = requests.get(url=url,params=param,headers=head)
    # page = respone.text
    # fileName = kw + '.html'
    # with open(fileName,'w',encoding='utf-8')as fn:
    #     fn.write(page)
    # print('爬取完成')
    #

    url = "https://fanyi.baidu.com/v2transapi?"
    params = input('输入:')
    data = {
        'query': params
    }
    response = requests.post(url=url,data=data,headers=head)
    dic = response.json()
    filename = params+".json"
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic,fp=fp,ensure_ascii=False)


if __name__ == '__main__':
    main()