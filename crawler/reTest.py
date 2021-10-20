#-*- codeing = utf-8 -*-
#@Time : 2021/5/28 下午2:22
#@Author : yuming shen
#@File : reTest.py
#@Software :PyCharm

import re

pat = re.compile("AA")   #创建模式用来验证的 预编译
# m = pat.search("WWSAa")
m = pat.search("asasAAcv")  #被验证 全文查找一次
pat = re.match("AA")      #查找开始的第一个
pat = re.search("AA")
#没有模式。 前面定义规则，后面查找的对象
m = re.search('AB','DDEavABrd')
print(m)
#替换
r = re.sub("aa","AA", "dsddffaa定时发放")
print(r)