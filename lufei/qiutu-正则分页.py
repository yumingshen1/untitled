#-*- codeing = utf-8 -*-
#@Time : 2021/7/8 下午3:16
#@Author : yuming shen
#@File : qiutu-正则.py
#@Software :PyCharm
import requests
import re
import os

#正则匹配图片
findimage = re.compile(r'<img src="(.*?)" alt=.*?>',re.S)

def main():

    #文件夹存在使用，不存在创建
    # if os.path.exists('/Users/shenyuming/Downloads/sym/tuwen/qiutu/'):
    #     os.mkdir('/Users/shenyuming/Downloads/sym/tuwen/qiutu/')

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

    #创建通用url
    url = 'https://www.qiushibaike.com/8hr/page/%d/'
    for pagenum in range(1,14):
        new_url = format(url%pagenum)

        #使用通用爬虫对整张页面进行爬取,提取整张页面内容
        response_text = requests.get(url=new_url,headers=headers).text
        img_list = re.findall(findimage,response_text)
        print(img_list)
        #循环取出list的数据，拼接成完整的url
        for src in img_list:
            src = 'https:'+src  #拼接
            print(src)
            img_link = requests.get(url = src,headers=headers).content   #图片二进制
            img_name = src.split('/')[-1]  #提取后缀为图片名字
            img_path = '/Users/shenyuming/Downloads/sym/tuwen/qiutu/'+img_name
            #保存图片
            with open(img_path,'wb') as fp:
                fp.write(img_link)
                print(img_name,'下载成功')


if __name__ == '__main__':
    main()
    print("爬取完成！")