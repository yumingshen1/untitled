# -*- coding:utf-8 -*-
# @Time : 2022/5/24 13:33
# Auther : shenyuming
# @File : 提取不重复的整数.py
# @Software : PyCharm

'''
提取不重复的整数，
'''
n = input()
n = n[::-1] #翻转字符串
list = []
for i in n:
    if i not in list:
        list.append(i)
    else:
        continue
for i in list:
    print(i)