# -*- coding:utf-8 -*-
# @Time : 2022/5/24 10:49
# Auther : shenyuming
# @File : string_len.py
# @Software : PyCharm

def lenn(str):
    string = input(str)
    string_list = string.strip().split(' ')
    list_1 = string_list[-1]
    print(len(list_1))

if __name__ == '__main__':
    lenn('hello word')