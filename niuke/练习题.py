# -*- coding:utf-8 -*-
# @Time : 2022/5/23 17:06
# Auther : shenyuming
# @File : 练习题.py
# @Software : PyCharm

## 求1-100的和
a = 0
for i in range(1,101):
    a=a+i
print(a)


##冒泡排序,算法

def bubblestor(a):
    l = len(a)
    for i in range(l):
        for j in range(0,l-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
a = [64, 34, 25, 12, 22, 11, 90]
bubblestor(a)
print('排序后的组：')
for i in range(len(a)):
    print('%d'%a[i])

## 冒泡排序，函数
b = [11,9,18,6,3,70,22]
bb = sorted(b)
print('函数sorted的从小到大排序：',bb)

c = [9,8,17,22,1,3,5]
c.sort(reverse=False)
print('函数sort排序',c)


print('字符串转成列表')
str = 'hello word'
li = str.split(' ')
print(li)