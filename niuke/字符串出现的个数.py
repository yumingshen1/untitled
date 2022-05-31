# -*- coding:utf-8 -*-
# @Time : 2022/5/24 19:04
# Auther : shenyuming
# @File : 字符串出现的个数.py
# @Software : PyCharm
try:
    string_1 = input()
    string_1.upper()    #统一变为大写
    string_list = list(string_1) #变为list,方便遍历

    check = input() ##输入查找的字符
    check.upper()   #变为大写
    num = 0
    for word in string_list:
        if word == check:
            num += 1
    print(num)
except Exception:
    print(';/////')