import random
import sys

import numpy

lists = [1,2,3,4,5]
def fun(x):
    return x**2
res = map(fun,lists)
print(res)
res = [i for i in res if i > 10]
print(res)

print('生成10-100之间的随机整数',random.randint(10,100))
print('生成5个随机小数',numpy.random.randn(5))
print('生成0-1之间的随机小数',random.random())


s = 'ajldjlajfdljfddd'
s1 = set(s)  #去重
print(s1)
s2 = list(s1) #强转为list
print(s2)
s2.sort(reverse = False)
res = "".join(s2)
print(res)
sum = lambda a,b :a*b
print(sum(4,5))


dic = {"name":"zs","sex":"man","city":"beijing"}
#字典转列表嵌套元祖
foo = zip(dic.keys(),dic.values())
foo  = [i for i in foo]
print(foo)
#字典嵌套元祖排序
b = sorted(foo,key=lambda x:x[0],reverse=False)
print(b)
#排序完构造新字典
new_dict = {i[0]:i[1] for i in b}
print(new_dict)

li = sorted(dic.items(),key = lambda x:x[0],reverse=False)
print(li)
print(dict(li))
news_dict ={i[0]:i[1] for i in li}
print(news_dict)

#正数从小到大，负数从大到小】（传两个条件，x<0和abs(x)）
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:(x<0,abs(x)))
print(a)

#列表嵌套字典的排序，分别根据年龄和姓名排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
a =sorted(foo,key=lambda x:x['name'],reverse=True)
b =sorted(foo,key=lambda x:x['age'],reverse=False)
print(a)
print(b)
print('+++++++++++')


example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list, key=lambda x:x*-1)
print(result_list)


list1 = ['asd','sdf','freg','sfag','refv','aser','sdfr','dfgi']
rt_list = []
for i in list1:
    if 's' in i:
        rt_list.append(i)
print(rt_list)
#列表生成式
rt_list2 = [x for x in list1 if 's' in x]
print(rt_list2)

#统计出现的次数
from collections import Counter
a = "programming,uhhhhjsdsq,qqqopoaaa"
res = Counter(a)
print(res)

import re
a = 'not 404 found 张三 99 深圳'
list3 = a.split(" ")
print(list3)
res = re.findall('\d+|[a-zA-Z]]+',a)
for i in res:
    if i in list3:
        list3.remove(i)
new_str = " ".join(list3)
print(res)
print(new_str)

#filter过滤序列
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(s):
    return s % 2 ==1
newlist = filter(is_odd,s)
newlist = [i for i in newlist]
print(newlist)


import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+' 星期：'+str(datetime.datetime.now().isoweekday())
print(a)
print(datetime.datetime.now())
#题https://www.cnblogs.com/finer/p/12846475.html

##自定义raise抛出异常
def fun():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)
fun()


#numpy矩阵,flatten方法
a = [[1,2],[3,4],[5,6]]
n = numpy.array(a).flatten().tolist()
print(n)
x = [j for i in a for j in i]
print(x)

x = 'abc'
y = 'def'
z = ["z","x","c"]
print(x.join(y))
print(x.join(z))


a = [1,2,3]
b = [4,5,6]
res = a+b
print(res)
a.extend(b)
print(a)

import copy
a = '哈哈'
b = a
c = copy.copy(a)
print(a,id(a))
print(b,id(b))
print(c,id(c))

a = [1,2,3,4,['a','b']]
b = a
c = copy.copy(a)
a.append(5)
a[4].append('c')
print(a,id(a))
print(b,id(b))
print(c,id(c))

#两种方式去除空格
str = "hellow word ha ha"
res = str.replace(" ","")
print(res)
res_list = str.split(" ")
print(res_list)
res = "".join(res_list)
print(res)

##应用数据分析库pandas,读取Excel文件的方法
import pandas as pd
df = pd.read_excel('/Users/shenyuming/Desktop/pandas.xlsx')
print(df)
#将pandas数据写入新的pandas_new的excel文件中，
df.to_excel("/Users/shenyuming/Desktop/pandas_new.xlsx",sheet_name='student')

#list
list5 = [1,2,3,4,5]
print(id(list5))
list5[1] = 6
print(id(list5))
#引用计数数量
print(sys.getrefcount(list5))

#去重
a=[1,2,4,2,4,5,6,5,7,8,9,0]
a = set(a)
print(a)

dict1 = {'a': 'no1', 'b': '2222'}
print(dict1.items())

#列表转字典
a = ['a1','a2']
b = ['b1','b2']
c = zip(a,b)
print(dict(c))

d = [a,b]
print(dict(d))

##字典转列表
dict_d = {
    '1':'a',
    '2':'b',
    '3':'c'
}
print(list(dict_d))
print(list(dict_d.keys()))
print(list(dict_d.values()))
print(list(dict_d.items()))

##字典转元组
dict5 = {
    'name':'ss',
    'age':'18'
}
print(tuple(dict5))
print(tuple(dict5.keys()))
print(tuple(dict5.values()))
print(tuple(dict5.items()),'===')


a = [1,2,4,2,4,5,6,5,7,8,9,0]
b = {}
b = b.fromkeys(a)
c = list(b.keys())
c.sort()
print(c)

print('===')
def first_chart(str):
    dict1 = {}
    for i in range(len(str)):
        #累计字符出现的次数
        if str[i] in dict1:
            dict1[str[i]]+=1
            #只出现一次，key对应的value就记录一次
        else:
            dict1[str[i]] = 1
    for i in range(len(str)):
        if dict1[str[i]] == 1:
            return str[i],i+1
str1 = input('输入字符串:')
print(first_chart(str1))

