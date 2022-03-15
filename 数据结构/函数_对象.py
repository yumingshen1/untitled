# -*- coding:utf-8 -*-
# @Time : 2022/1/22 17:19
# Auther : shenyuming
# @File : 函数_对象.py
# @Software : PyCharm
'''
    定义函数与调用函数
函数的返回值
函数中的形参与实参,函数的缺省值
可变长度参数,关键字参数
字符串的find()方法,index()方法
strip()方法,replace()方法,split()方法
'''

def function1():
    print('函数1')
    return 3
function1() #打印函数内的语句
print('打印函数返回值',function1()) # 打印函数返回值

def function2(a,b):
    return a*b
print('形参传值',function2(2,3))

def function3(a,b=5):
    return a+b
print('形参+缺省值',function3(3))
print('形参+缺省值赋值',function3(5,10))

def function4(n):
    if n > 3:
        return n,10  #return可以返回多个值，是一个元组
    else:
        return -n
print('return返回多个值是元组形式：',function4(5))

def function5(v,m):
    return [v+m,v*m,m]
print('return以列表形式返回：',function5(3,5))


print("---------可变参数--------")
def function6(a,*args):
    return a,args
print('形参+可变长度参数：',function6(2,10,50,100))

def function7(a,*args):
    return (a,*args)
print('形参+可变长度参数--解包--少一层元祖：',function7(2,10,50,100))

def function8(a,*args):
    return (a,a*args)       ## a*args = 多少次
print('args多少次：',function8(2,10,20,30))

def function9(*args):
    return args
print('单独打印args是元组',function9(2,3,5,6))


print("--------关键字参数--------")

def function10(**kwargs):
    return kwargs
print(function10(name='shen',age=18))


## 身份证输入

def idCar(num):
    lenght = len(num)
    print('您输入的长度：',lenght)
    if len(num)!=18:
        print('长度不对')
    elif not num[0:16].isdigit():
        print('前17位有的不是数字')
    elif not num[-1].isdigit() and num[-1] not in ['X','x']:
        print('最后一位不对')
    else:
        if int(num[-2]) % 2 == 0:
            print('女性')
        elif int(num[-2]) % 2 != 0:
            print('男性')
        else:
            print('人妖？')

num='123456789101234567'
# idCar(num)


str1 = 'skdjisudfndsbfjherjsf'
print('index()从3位置开始查找某个字符串的下标:',str1.index('s',3))
print('find()从2位置开始查找某个字符串下标查找',str1.find('j',2))

str2 = 'qwertuikd '
print('去除首尾空格',str2.strip())
print('去除首尾特定字符',str2.strip('q'))

print('替换某些值：',str2.replace('ik','ASD'))

str3 = 'aesdrftgikawsertgk'
print('以指定字符默认分割',str3.split('k'))
print('以指定字符分割2次',str3.split('s',2))


name = 'A girl come in, the name is Jack, level 955;'
def getName(str):
    return str.split('is')[-1].split(',')[0].replace(' ','')
print(getName(name))

