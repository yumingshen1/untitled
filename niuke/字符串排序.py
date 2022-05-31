# -*- coding:utf-8 -*-
# @Time : 2022/5/24 17:38
# Auther : shenyuming
# @File : 字符串排序.py
# @Software : PyCharm

'''
    字符串排序，按照字典序列排序
'''
num = int(input())
list = []
for i in range(num):
    list.append(input())
list.sort()

for i in list:
    print(i)