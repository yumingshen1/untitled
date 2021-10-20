#-*- codeing = utf-8 -*-
#@Time : 2021/6/30 下午5:40
#@Author : yuming shen
#@File : movies_crawler.py
#@Software :PyCharm

import urllib.request,urllib.error
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import xlwt
import json
import time

#访问爬取数据，
#解析数据
#保存数据

def main():

    url = 'https://movie.douban.com/top250?start='

    #ask(url)

    #得到数据，并解析数据
    datalist = getData(url)

    #存储数据到excel
    # save_excel_path = r'./电影数据.xls'
    # save_excel(datalist,save_excel_path)

    #保存图片
    datalist_image = getimage(url)


#使用正则预编译查找的数据
find_name = re.compile(r'<span class="title">(.*?)</span>')
find_link = re.compile(r'<a href="(.*?)">')
find_image = re.compile(r'<img.*"(.*?)" width="100"/>',re.S)
find_score = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_ms = re.compile(r'<span class="inq">(.*)</span>')

def getData(url):
    datalist = []
    for i in range(0,10):
        url = url+str(i*25)+"&filter="
        html = ask(url)   #调用单个页面的爬取，存成html
        #每爬取一条解析一条
        soup = BeautifulSoup(html,'html.parser')   #已html.parser方式解析

        for item in soup.find_all('div',class_="item"):
            data = []    #存放每一条数据
            item = str(item)
            #查找片名
            title = re.findall(find_name,item)[0]
            data.append(title)
            #查找地址
            link = re.findall(find_link,item)[0]
            data.append(link)
            #查找图片
            image = re.findall(find_image,item)[0]
            data.append(image)
            #查找评分
            score = re.findall(find_score,item)[0]
            data.append(score)
            #查找描述
            ms = re.findall(find_ms,item)
            if len(ms)!= 0:
                ms = ms[0].replace("。","")
                data.append(ms)
            else:
                data.append(" ")

            datalist.append(data)

    return datalist


def getimage(url):
    datalist_image = []
    for image in range(0,10):
        time.sleep(2)
        page = image * 25
        urlStr = url+str(page)+"&filter="
        html = ask(urlStr)
        soup = BeautifulSoup(html, 'html.parser')  # 已html.parser方式解析
        images = soup.find_all('div', class_="pic")
        length = len(images)
        for key in range(length):
            item = str(images[key])
            # 查找图片
            image = re.findall(find_image, item)[0]
            file_name = image.split('/')[-1]
            # imgnum = page + key
            urllib.request.urlretrieve(image,'/Users/shenyuming/Downloads/sym/tuwen/mv/'+file_name+'.jpg')


#爬取数据
def ask(url):
    head = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    html = " "
    re = urllib.request.Request(url=url,headers=head) #封装请求反反扒
    try:
        response = urllib.request.urlopen(re)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.HTTPError as ht:
        print(ht.code,ht.reason,ht.headers, sep='\n')
    except urllib.error.URLError as ul:
        print(ul.reason)

    return html


def save_excel(datalist,save_excel_path):
    print('开始保存到excel')
    #创建excel
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    col = ("片名","地址","图片","评分","描述")
    #将标题循环写入
    for i in range(0,5):
        sheet.write(0,i,col[i])
    #循环写入数据
    for n in range(0,250):
        #datalist的数据拿出放入data准备写入
        print('第%d条'%(n+1))
        data = datalist[n]
        for j in range(0,5):
            sheet.write(n+1,j,data[j])
    workbook.save(save_excel_path)


def save_db(url,path):
    pass

if __name__ == '__main__':
    main()
    print('爬取完毕！')