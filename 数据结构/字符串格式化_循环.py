# -*- coding:utf-8 -*-
# @Time : 2022/1/22 19:30
# Auther : shenyuming
# @File : 字符串格式化_循环.py
# @Software : PyCharm
'''
    %s的用法
.format的用法
f''的用法
for循环,while循环
break语句,continue语句
循环的else语句
循环语句实现倒计时程序
'''

a = 5
b = 6
print('a'+'+'+'b'+'=',a+b)

def asc(a,b,c,d):
    return ('%d,%s,%f,%d'%(a,b,c,d))
print(asc(2,'str',33.567,9))

def asc2(a,b,c):
    return ('%3d,%-15f,%s'%(a,b,c))
print('%3d-右偏移3位，%-15f左偏移15位，%s正常显示-->：',asc2(5,33.1233233,'good'))

def asc3(a,b,c):
    return ('%03d,%010.3f,%-5s'%(a,b,c))
print('%03d右对齐，左侧补0； %010.3f右侧对齐共10位，左侧补0，小数保留3位；%-5s左侧对齐，右侧补空 ',asc3(12,23.56,'off'))



def asc4():
    return ('wsdsj{},djskj{}'.format('AS',22))
print('.format格式化:',asc4())

def asc5(a,b):
    return ('wsdsj{:10},djskj{:0<5}'.format(a,b))
print('{:10}字符串左对齐 ；  {:0<5}数字左对齐不足补0--->:',asc5('WSA',2))


name1 = 'UI'
name2 = 50
def asc6(name1,name2):
    return (f'名字1是：{name1:10},名字2是：{name2:@>10}')
print(asc6(name1,name2))

## 题
# input = input('请输入：')
# studentstr = input.split(';')
# print('学生信息：',studentstr)
# for one in studentstr:
#     if one != '':
#         name = one.split(',')[0]
#         age = one.split(',')[1]
#         name = name.strip()
#         age = age.strip()
#         print(f'name is {name:<20},年龄 is {age:>2}')


## 循环
lista = ['gy','zf','zl','lb']
for i in lista:
    print('直接循环lista值：',i)

for i in range(len(lista)):
    print('循环lista的长度：',lista[i])


for i in range(1,10):
    if i == 5:
        continue
    print('i的值：',i)
else:
    print('continue执行完后，继续执行else')


##倒计时

import time
for i in range(10,0,-1):
    print(f'\r倒计时{i}',end = '')  # \r是将光标回到首位，end='' 不换行
    time.sleep(1)
else:
    print(f'\r倒计时结束！')


log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0	
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0	
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0	
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0	
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0	
f20180111090619/i_3BKlsRaZ.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156330575626044	image/jpeg	0	
f20180111090619/i_5XboXSKh.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156329453409855	image/jpeg	0	
f20180111090619/i_6DiYSBKp.jpg	74017	FrYG3icChRmFGnWQK6rYxa88KuQI	15156329461803290	image/jpeg	0	
f20180111090619/i_76zaF2IM.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156334738356648	image/jpeg	0	
f20180111090619/i_B6TFYjks.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156329464034474	image/jpeg	0	
f20180111090619/i_N9eITqj3.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156330419595764	image/jpeg	0	
'''
dict = {}
line_list = log.split('\n')
print(line_list)
for one in line_list:
    if one !='':
        one1 = one.split('\t')[0] #获得类型字段
        file_type = one1.split('.')[1] #获得后缀
        file_size = int(one.split('\t')[1]) #获得大小字段,转为int类型
        if file_type not in dict:
            dict[file_type] = file_size
        else:
            dict[file_type] += file_size
print(dict)

