# -*- coding:utf-8 -*-
# @Time : 2022/5/24 15:39
# Auther : shenyuming
# @File : 句子逆序.py
# @Software : PyCharm
def strr(str):
    string = list(input(str).strip().split())
    string.reverse()
    print(" ".join(string))
s = 'i AM IS BOY'
strr(s)