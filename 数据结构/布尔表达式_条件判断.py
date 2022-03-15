# -*- coding:utf-8 -*-
# @Time : 2022/1/22 17:06
# Auther : shenyuming
# @File : 布尔表达式_条件判断.py
# @Software : PyCharm

'''
    布尔值True,False的意思
in,not in
and,or
not,and,or的优先级
'''


print('a' == 'A')
print('a' > 'A')    #ASCII 比较，一般小写值大于大写值
print('aA' > 'Aa')  #只比较第一位，第一位相同时，比较第二位，

list1 = [100,200,232,300,[201,303,505],309]
print(100 in list1)
print(200 in list1[4])
print(300 not in list1[-2])

print(3>2 or 1==0 or 5>3)   #or 一真为真，全假为假
print(2>2 and 9<3 and 5>3)  # and 一假为假，全真为真

