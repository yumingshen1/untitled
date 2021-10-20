#-*- codeing = utf-8 -*-
#@Time : 2021/7/11 下午9:49
#@Author : yuming shen
#@File : city-xpath.py
#@Software :PyCharm

import requests
from lxml import etree

def main():
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)

    #分开获取，加入list统一存储
    # all_city_name = []
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # for hotcity in hot_li_list:
    #     hotcityname = hotcity.xpath('./a/text()')[0]
    #     all_city_name.append(hotcityname)
    #
    # all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for allcity in all_li_list:
    #     allcityname = allcity.xpath('./a/text()')[0]
    #     all_city_name.append(allcityname)
    # print(all_city_name,len(all_city_name))

    #一个xpath获取全部数据,页面不同的数据的xpath 可以用 ｜ 来同时查找
    all_city = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    all_name = []
    for a in all_city:
        all_cityname = a.xpath('./a/text()')[0]
        # print(all_cityname)
        all_name.append(all_cityname)
    print(all_name,len(all_name))

if __name__ == '__main__':
    main()