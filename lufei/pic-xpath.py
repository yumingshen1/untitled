#-*- codeing = utf-8 -*-
#@Time : 2021/7/11 下午6:17
#@Author : yuming shen
#@File : pic-xpath.py
#@Software :PyCharm

import requests
from lxml import etree
import os

def main():

    url = 'https://pic.netbian.com/4kmeinv/'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    #请求获取数据
    respone = requests.get(url=url,headers=headers)
    # 获取页面原始编码格式
    # print(respone.encoding)
    #设置编码格式
    # respone.encoding='utf-8'
    page_text = respone.text

    #解析数据
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('/Users/shenyuming/Downloads/sym/tuwen/piclibs'):
        os.mkdir('/Users/shenyuming/Downloads/sym/tuwen/piclibs')

    for li in li_list:
        img_url = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        #以alt的文字为图片名
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        #将乱码对应的数据已encode('iso-8859-1').decode('gbk')方式编码
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        #请求图片地址,二进制
        img_data = requests.get(url=img_url,headers=headers).content
        #保存路径
        img_path = '/Users/shenyuming/Downloads/sym/tuwen/piclibs/'+img_name
        with open(img_path,'wb')as fp:
            fp.write(img_data)
            print(img_name+'下载完成！！')


#encoding encode decode codeing
if __name__ == '__main__':
    main()