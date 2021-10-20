#-*- codeing = utf-8 -*-
#@Time : 2021/5/25 下午5:40
#@Author : yuming shen
#@File : spider.py
#@Software :PyCharm

import re   #正则匹配
from bs4 import BeautifulSoup #网页解析。数据获取
import urllib.request,urllib.error  #指定url获取网页数据
import xlwt  #excel操作
import sqlite3   #sqlite数据库操作
import pprint

def main():
    baseurl = "https://movie.douban.com/top250?start="

    # 1爬取网页
    datalist = getData(baseurl)
    askURL(baseurl)

    #保存excel地址
    #savepath = r"/Users/shenyuming/Downloads/python/豆瓣top250.xls"

    #保存数据库地址
    savedb = "movietest.sqlite"

    # 3保存数据到excel
    #saveDate(datalist,savepath)

    # 3保存数据到数据库
    saveDateDB(datalist,savedb)

#定义正则 预编译
findlink = re.compile(r'<a href="(.*?)">')
findname = re.compile(r'<span class="title">(.*)</span>')
findImage = re.compile(r'<img.*src="(.*?)"',re.S)
#评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJude = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#1爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):  #循环10次，将每个页面都循环到
        url = baseurl + str(i*25)    #URL拼接，将每个页面的start=?拼接到
        html = askURL(url)        #调用爬取url网页函数

        # 2解析数据  以html.parser方式解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_='item'): #查找每一部电影符合要求的字符串.形成列表
            data = [] #准备列表存储每一部的资源
            item = str(item) #转换成字符串比较
            #地址链接
            link = re.findall(findlink,item)[0]
            data.append(link)
            #图片
            image = re.findall(findImage, item)[0]
            data.append(image)
            #评价人数
            jude = re.findall(findJude, item)[0]
            data.append(jude)
            #评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            #名字
            name = re.findall(findname,item)
            if(len(name)==2):
                cname = name[0]
                data.append(cname)
                oname = name[1].replace("/","")  #<span class="title"> / The Shawshank Redemption</span> 外国名字有特殊符号 "/"要去掉
                oname = oname.replace("'", "")
                data.append(oname)
            else:
                data.append(name[0])
                data.append(' ')  #如果没有外国名就填入空

            #剧情描述
            # inq = re.findall(findInq,item)
            # if len(inq)!=0:
            #     inq = inq[0].replace("。","")     #<span class="inq">希望让人自由。</span> 不想要最后的句号，去掉
            #     inq = inq.replace("'",'"')
            #     data.append(inq)
            # else:
            #     data.append(" ")

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = re.sub("[。|']", "",inq[0])  # <span class="inq">希望让人自由。</mspan> 不想要最后的句号，去掉
                data.append(inq)
            else:
                data.append(" ")


            #导演主演
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/> 替换成空格
            bd = re.sub('/'," ",bd)
            bd = re.sub("'"," ",bd)
            # bd = bd.replace('<br>'," ")  #replace不适用于当前的替换，replace适用于字符串的替换，需要去除多余换行空格用正则匹配
            # bd = bd.replace("/"," ")

            data.append(bd.strip())

            datalist.append(data) #将一部电影的信息都存到datalist

    # for i in datalist:
    #     print(i)
    # print(datalist,end="\n")
    return datalist


##得到一个指定url的网页内容
def askURL(url):
    head={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        respone = urllib.request.urlopen(request)
        html = respone.read().decode('utf-8')
        print(html)
    except Exception as e:
        print(e)
    return html


#3保存数据到excel
def saveDate(datalist,savepath):
    print("save...")
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","评价人数","评分","中文名字","影片外文名","剧情描述","导演主演",)
    for i in range(0,8):  #循环将每列标题写入
        sheet.write(0,i,col[i])
    for i in range(0,250):  #写入爬取的数据
        print("第%d条"%i)
        data = datalist[i]  #循环取出每一条放进data
        for j in range(0,8): #循环写入每一条数据中的内容，
            sheet.write(i+1,j,data[j])
    book.save(savepath)  #保存excel

#保存到数据库
def saveDateDB(datalist,savedb):
    init_db(savedb)
    conn = sqlite3.connect(savedb)
    cursor = conn.cursor()

    for data in datalist:
        for index in range(len(data)): # 循环索引
            if index == 2 or index == 3:
                continue
            data[index] = "'"+data[index]+"'"  #给每列加双引号变为字符型
        sql = 'insert into movie250(info_link,pic_link,findJude,findRating,cname,enama,findInq,info) values(%s)'%",".join(data)
        cursor.execute(sql)
    conn.commit()
    conn.close()

#数据库初始创建表
def init_db(dbpath):
    sql = '''
        create table IF not exists movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        findJude numeric,
        findRating numeric,
        cname varchar,
        enama varchar,
        findInq text,
        info text     
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    # init_db("movie.db")
    print('爬取完毕！')
