#-*- codeing = utf-8 -*-
#@Time : 2021/6/27 下午3:33
#@Author : yuming shen
#@File : Movies-Request.py
#@Software :PyCharm

import requests
import json

def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    head = {
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.114Safari / 537.36"
    }
    data = {
        "type": 24,
        "interval_id": "100:90",
        "action":'',
        "start":"0",
        "limit":"20"
    }
    respone = requests.get(url=url,params=data,headers=head)
    list_data = respone.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!!')


if __name__ == '__main__':
    main()