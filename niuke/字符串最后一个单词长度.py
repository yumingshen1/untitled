# -*- coding:utf-8 -*-
# @Time : 2022/5/24 18:56
# Auther : shenyuming
# @File : 字符串最后一个单词长度.py
# @Software : PyCharm

n= input('hello word')
n = n.strip().split()  #split返回一个列表
word_list = n[-1]
print(len(word_list))

