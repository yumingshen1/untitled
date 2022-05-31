# -*- coding:utf-8 -*-
# @Time : 2022/5/24 18:28
# Auther : shenyuming
# @File : int整数内存中的1的个数.py
# @Software : PyCharm

''''
    查询int整形数据在内存中存储时1的个数
'''
try:
    n = int(input())
    num = 0
    if n <= 0:
        raise Exception
    bin_number = bin(n) #转成二进制字符串
    result_number = bin_number.count('1')   #查找1的个数
    print(result_number)
except Exception:
    exit()
