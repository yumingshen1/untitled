# -*- coding:utf-8 -*-
# @Time : 2022/5/24 13:11
# Auther : shenyuming
# @File : 合并表记录.py
# @Software : PyCharm
'''
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）
'''
n = int(input())
dic = {}
for i in range(n):
    number = input()
    number = number.split()
    key = int(number[0])
    value = int(number[1])
    if key in dic:
        dic[key] +=value
    else:
        dic[key] = value
for key,value in sorted(dic.items()):
    print(key,value)
