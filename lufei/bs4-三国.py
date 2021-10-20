#-*- codeing = utf-8 -*-
#@Time : 2021/7/9 下午2:06
#@Author : yuming shen
#@File : bs4-三国.py
#@Software :PyCharm
import requests
from bs4 import BeautifulSoup
import urllib.request
import time

def main():
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    headers = {"User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.114Safari / 537.36",
               "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh - CN, zh",
                "accept": "text / html, application / xhtml + xml, application / xml;"
    }
    #request请求
    r = requests.get(url=url,headers=headers)
    r.encoding = 'utf-8'
    page_text = r.text
    print(page_text)

     #urllib请求
    # re_url = urllib.request.Request(url=url,headers=headers)
    # respone = urllib.request.urlopen(re_url)
    # page_text = respone.read().decode('utf-8')
    # print(page_text)

    # 实例化BeautifulSoup对象，将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'html.parser')
    #解析标题和详情内容,select选择标签属性为book-mulu的开始往下找
    li_list = soup.select('.book-mulu > ul > li')
    print(li_list)
    fp = open('/Users/shenyuming/Downloads/sym/tuwen/sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        #对详情页发出请求，urllib请求
        detail_re = urllib.request.Request(url=detail_url,headers=headers)
        detail_text = urllib.request.urlopen(detail_re)
        detail_d = detail_text.read().decode('utf-8')
        #request请求
        # detail_page_text = requests.get(url=detail_url,headers=headers)
        # detail_page_text.encoding = 'utf-8'
        # detail_con = detail_page_text.text
        # 解析详情数据
        detail_soup = BeautifulSoup(detail_d,'lxml')
        div_tag = detail_soup.find('div',class_="chapter_content")
        #获取改标签下的所有文本
        content = div_tag.text
        time.sleep(1)
        fp.write(title+":"+content+"\n")
        print(title+"下载完成！")


if __name__ == '__main__':
    main()