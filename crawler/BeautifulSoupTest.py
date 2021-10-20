#-*- codeing = utf-8 -*-
#@Time : 2021/5/26 下午6:03
#@Author : yuming shen
#@File : BeautifulSoupTest.py
#@Software :PyCharm
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent)
# print(soup.head)
# print(soup.get_text)
# for flk in soup.find_all('a'):
#     print(flk.get('href'))
#     print(flk)
# print(soup.body.b)
# print(soup.a)
# print(soup.find_all('a'))
#
# head_tag = soup.head
# print(head_tag)
# print(head_tag.contents)
# print(head_tag.contents[0])
#
# title_tag = head_tag.contents[0]
# print(title_tag.contents)
#
# for children in title_tag.children:
#     print (children)
#
# for chilen in head_tag.descendants: #循环所有子节点
#     print(chilen)
#
# for string in soup.strings:  #循环所有字符串
#     print(string)
#
# for string in soup.stripped_strings:  #循环所有字符串去掉多余空格空行
#     print(string)
# print(len(soup.contents))
# print(soup.contents[0].name)
#
# #2 kwargs   参数查找
# t_list = soup.find_all(href="http://example.com/lacie")
# for item in t_list:
#     print(item)
#
# # 3 text 参数
# t_list = soup.find_all(text="xxxxxxxx")
# for item in t_list:
#     print(item)
#
# # css选择器
# t_t = soup.select('title')     #标签查找
# for it in t_t:
#     print(it)
#
# t_t = soup.select('.story')     #类名查找,class=story
# for it in t_t:
#     print(it)
#
# t_t = soup.select('#link1')     #id查找,id=link1
# for it in t_t:
#     print(it)
#
# t_t = soup.select('p[class="title"]')     #属性查找, <p下的class=title属性
# for it in t_t:
#     print(it)
#
#
# t_t = soup.select('p>b')     #子标签查找, 从副标签往下找 父>子
# for it in t_t:
#     print(it)
#
# t_t = soup.select('.title ~ .story')  #按兄弟标签查找。title和story在同一级别，找到story级别的文本
# print(t_t[0].get_text())

import re
# for tag in soup.find_all(re.compile('t')):   #正则表达式超找
#     print(tag)


##定义一个方法查找，方法只接受一个元素参数，调用无需传值
#查找包含class属性且不包含id属性的标签
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
rr = soup.find_all(has_class_but_no_id)
print(rr)

def not_lacie(href):
    return href and not re.compile("lacie").search(href)
rs = soup.find_all(href=not_lacie)
print(rs)

#按ID= true 查询，不论ID的值
print(soup.find_all(id =True))

#按多个属性值搜索
print(soup.find_all(href=re.compile("elsie"), id='link1'))

##些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
#但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
soup.find_all(attrs={"data-foo": "value"})


##按css搜索 a标签所有包含class=sister的数据
soup.find_all("a", class_="sister")
# or 函数方式
def cs(x,y):
    return soup.find_all(x,class_=y)
print(cs('a','sister'))



