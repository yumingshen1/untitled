#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午6:23
#@Author : yuming shen
#@File : request-cookie.py
#@Software :PyCharm

import requests
from lxml import etree
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
#登陆
url = 'https://github.com/login'
#创建session会话对象
session = requests.Session()
#使用会话对象发起登陆请求
page_text = session.get(url=url,headers=headers).text
#解析出动态的taken值
tree = etree.HTML(page_text)
t = tree.xpath('//div[@id="login"]/div[4]/form/input[1]/@value')[0]
#指定模拟登陆请求的url
detail_url = 'https://github.com/session'
#封装参数
data = {
'commit': 'Sign in',
 'utf8': '✓',
 'authenticity_token': t,
 'login': 'm18515607030@163.com',
 'password': 'Sym123456789',
 'webauthn-support': 'supported',
}
#使用会话对象进行模拟登陆
page_text = session.post(url=detail_url,headers=headers,data=data).text
#存储
with open('./github.html','w',encoding='utf-8') as f:
    f.write(page_text)