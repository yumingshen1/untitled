# -*- coding:utf-8 -*-
# @Time : 2022/5/24 21:09
# Auther : shenyuming
# @File : 删除字符串中出现次数最少的字符.py
# @Software : PyCharm


str = input()
dic = {}
for i in str:
    if i not in dic:
        dic[i] = str.count(i)
min = min(dic.values())  ##最少的字典值
for k ,v in dic.items():
    if v == min:
        str = str.replace(k,'')
print(str)