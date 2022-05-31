# -*- coding:utf-8 -*-
# @Time : 2022/5/24 12:11
# Auther : shenyuming
# @File : 取近似值.py
# @Software : PyCharm


n = float(input())
#整数
res = n // 1
#小数
tep = n - res
if tep >=0.5:
    print(int(res+1))
else:
    print(int(res))

