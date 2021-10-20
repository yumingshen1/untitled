#ord 获取字符的整数
print(ord('A'))

#chr 编码转换为字符
print(chr(65))

#格式化
print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('hi,%s ,you can the %s python.' % ('xiaoka','v3'))
print('hello,{0},成绩提升了吧{1}'.format('xxx',23.332))
# :后的.2f指定格式化参数 保留2位
print('hello,{0},成绩提升了吧{1:.1f}%'.format('xxx',23.332))

s1 = 72
s2 = 85
r = s1/s2*0.1
print(f'小明的成绩从去年的 {s1} 提升到了今年的 {s2:.1f}.')

#循环
names = ['a','b','c']
for name in names:
    print(name)

sum = 0
for i in [1,2,3,4,5,6,7]:
    sum = sum+i
print(sum)

sum = 0
for x in range(99):
    sum = sum+x
print(sum)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


#字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#使用get方法，没有value时返回自己定义的值
print(d.get('Thomas',-1))

#删除一个字典的key
d.pop('Bob')
print(d)


#定义函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(2))


#改进   内置函数isinstance()是否是已知类型的参数
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('type error')
    if x > 0:
        return x
    else:
        return -x
print(my_abs(22))


#函数的参数
#位置参数
def weizhicanshu(x):
    return x*x
print(weizhicanshu(5))
#x的多次方
def weizhicanshu2(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(weizhicanshu2(2,7))
print("...///////")

#默认参数
def morencanshu(x,n=2):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
        return s
print(morencanshu(5))

#可以只传入需要的参数
def morencanshu2(name, gender,age=6, city='beijing'):
    return name,"说年龄是：",age,"之后：",gender,city
print(morencanshu2("嗯额","F",8))


#可变参数, 传入值可以是list和tuple
def kebiancanshu(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
print(kebiancanshu([1,2,3]))
print(kebiancanshu((4,5,6)))

#利用 *args传入可变参数
def kabian(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(kabian(1,2,3,4,5,6))

#如已有的list和tuple，要调用可变参数可以在直接用 * 带入
nums = [1,2,3]
print(kabian(*nums))
nub = (1,2,3)
print(kabian(*nub))


#关键字参数 以字典形式传入 ， 可以扩展功能
def guanjianzi(name,age,**kw):
    print('name:',name ,'age:',age,'other:',kw)
#可以只传入必选参数
guanjianzi('f',12)
#可以传入任意个关键字参数
guanjianzi('名字',20,city = 'shanghai')

guanjianzi('名字',20,city = 'shanghai',job='大佬')

extra = {'city':'夜上海','job':'大佬啊'}
guanjianzi('茗',29,**extra)

##命名关键字参数，希望检查只有City和job的参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
print(person("shen",23,city='beijing',job = "可以"))

##如果要限制关键字参数名字，只接受city和job， *后代表只接受的参数
def MingMingGuanJianZi(name,age,*,city,job):
    if 1 > 2 :
        pass
    print('name:',name,'age:',age,"city:",city,"job:",job)
print(MingMingGuanJianZi("Me",25,city='beijing',job='IT'))

##递归函数 (函数在内部调用自己就是递归函数)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(100))

##切片
l = list(range(100))
print(l)
print(l[::5])
print(l[:50])
print(l[-2:])

###迭代
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)
##判断是否可以迭代 用collections模块的iterable类型判断   3.8中已停止使用
#from collections import Iterable
#isinstance('abc',Iterable)
#sinstance([1,2,3],Iterable)
#isinstance(123,Iterable)

##生成列表式
l = list(range(1,11))
print(l)

l = []
for i in range(1,11):
    l.append(i*i)
print(l)

ll = [x * x for x in range(1,11)]
print(ll)

ll = [x * x for x in range(1,11) if x % 2 == 0 ]
print(ll)

###生成器 []换成()
g = (x * x for x in range(10))
for n in g:
    print(n)


