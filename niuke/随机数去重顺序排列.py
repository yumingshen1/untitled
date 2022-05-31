# -*- coding:utf-8 -*-
# @Time : 2022/5/24 19:21
# Auther : shenyuming
# @File : 随机数去重顺序排列.py
# @Software : PyCharm
try:
    n_value = int(input())  #输入随机数的个数
    list = []
    for i in range(n_value):
        m_value = int(input())  #输入随机数
        list.append(m_value)        #随机数加入list中
    list_set = set(list)        #变为set去重
    list_2 = list(list_set) #再变为list
    list_2 = sorted(list_2)     #排序
    for i in list_2:
        print(i)
except Exception:
    print(',,,,')