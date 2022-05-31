# -*- coding:utf-8 -*-
# @Time : 2022/5/24 11:12
# Auther : shenyuming
# @File : 随机数去重.py
# @Software : PyCharm

## 生成随机数并去重
while True:
    try:
        n = input(3)
        lst = []
        for i in range(int(n)):
            lst.append(int(input()))
        lst2 = set(lst)  #去重 无序
        lst = list(lst2) #集合变为列表
        lst.sort()   #排序
        for i in lst:
            print(i)
    except:
        break

print('------------------')

n_value = input()
n_value = int(n_value)
list_1 = []
for i in range(0,n_value,1):
    number = int(input())
    list_1.append(number)
list_1 = set(list_1)
list_1 = list(list_1)
list_1 = sorted(list_1)
for value in list_1:
    print(value)