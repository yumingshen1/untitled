# -*- coding:utf-8 -*-
# @Time : 2022/1/22 15:42
# Auther : shenyuming
# @File : 字符串_列表_元组.py
# @Software : PyCharm

'''
    字符串的概念
    单引号,双引号,三引号的作用
    字符串的下标与切片

    列表的新增append,insert,extend
    列表的删除pop,remove,del
    列表的下标与切片
'''

'''
    了解单引号,双引号,三引号的作用
    会使用字符串的下标进行取值
    会使用切片对字符串取值
    
    会新增列表中的元素
    会修改列表中的元素
    会删除列表中的元素
    会使用下标对列表进行取值
    会使用切片对列表进行取值
'''

'''
    列表的增、删、扩展、修改，没有返回值，需要另行打印/获取 ，  pop除外，会获取删除的元素
'''
var1 = 'Hello World!'
print('字符串下标取值：',var1[2])
print('字符串切片取值：',var1[0:5])
print('字符串新增值：',var1+ 'xin')
print('字符串更新值：',var1[:6]+ 'zhi')
print('字符串删除元素：',var1.strip('H'))
print('字符串替换元素:',var1.replace(' ','-'))


listq = [1,2,'a','r',(1,2,3,4,5),{'as':'kl'}]
print('列表下标取值：',listq[3])
print('列表切片取值：',listq[4:])
print('列表切片取值：',listq[4][0:2])

listq.append(200)
print('新增列表中的元素:',listq)
listq.insert(1,'编码')
print('insert新增：',listq)

listb = [100,500]
listq.extend(listb)
print('extend合并：',listq)

listq[2] = 3
print('修改列表中的元素:',listq)

listq.pop(0)
print('删除列表中的元素:',listq)
del listq[2]
print('删除列表中的元素:',listq)
listq.remove(200)
print('删除列表中的元素:',listq)


tuple1 = (1,2,3)
tuple2 = (20,)
print('元组：',tuple1,tuple2)
tuple3 = (22,23,55,[2,50])  ##元祖中的列表值可以修改
tuple3[3][1]= 1
print(tuple3)
