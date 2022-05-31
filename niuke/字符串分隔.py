# -*- coding:utf-8 -*-
# @Time : 2022/5/24 19:42
# Auther : shenyuming
# @File : 字符串分隔.py
# @Software : PyCharm

try:
    while True:
        l = input()
        for i in range(0,len(l),8):
            print("{0:0<8s}".format(l[i:i+8]))
except Exception:
    print('ceshi')