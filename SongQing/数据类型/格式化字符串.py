
print('----字符串用%s-----整数用%d------浮点数用%f--------')
a=5
b=6
print('-------拼接------')
print('a'+'+'+'b'+'=',a+b)


print('------格式化字符串一 %d\%s\%f -----占位符数量与之后的参数数量不一致会报错--')
print('%d+%d=%d'%(a,b,a+b))
def sss(AA,BB,CC,X,Y):
    print('我是%s,你是%s，他是%s，今年是%d年，凌晨%f,'%(AA,BB,CC,X,Y))
sss('天乐','德华','学友',2021,22.2 )

##占位符多余 参数，报错
# info = f'我是%s,你是%s，他是%s，今年是%d年，'%('sss','ddd','fff')
# print(info)
##占位符少于 参数，报错
# info1 = f'我是%s,你是%s，他是%s，今年是%d年'%('aa','bb','cc',22,'ee')
# print(info1)

##前面用%d后面用%s，报错
# info3 = f'我是%d,你是%d，他是%d'%('22','23','20')
# print(info3)

##前面用%s后面用%d,不报错
info2 = f'我是%s,你是%s，他是%s'%(20,22,18)
print(info2)


print('-----%ns补位--默认右对齐----字符串本身超过n位，则显示全部字符串--')
print('我是%7s,你是%3s，他是%5s，今年是%10d年，'%('张xx','陈','也不知道是谁',202110))
print('我是%7s,你是%3s，他是%5s，今年是%010d年，'%('张xx','陈','也不知道是谁',202110))

print('------%-ns左对齐------')
print('我是%-4s,你是%-3s，他是%-5s，今年是%-8d年'%('张xx','陈','也不知道是谁',202110))
info5 = f'我是%-4s,你是%-3s，他是%-5s，今年是%-8d年'%('wqw','fd','sdwdasdwdad',10)
print(info5)


print('------%f浮点型，默认保留6位数----')
number = '您输入的数字是：%f'%(3.7)
print(number)

print('------%n.xf--n表示补齐多少位， x表示保留几位小数')
number2 = '您输入的数字是：%.2f'%(3.7) + "保留两位小数"
print(number2)
number2 = '您输入的数字是：%10.2f'%(3.7) + "补齐10位，右对齐，保留两位小数"
print(number2)
number2 = '您输入的数字是：%-10.2f'%(3.7) + "补齐10位，左对齐， 保留两位小数"
print(number2)



print('----------字符串格式化二--------{} .format')
str1 = 'my name is {},your name is {}'.format('yuming','xixi')
print(str1)

print('-----参数多余空位，不报错，顺序取值------')
str2 = 'my name is {},your name is {}，'.format('yuming','xixi','tt')
print(str2)

print('----------{}没有写数字时顺序取值，写了数字{1},{2},按下标取值， 不能混用------')
str3 = 'my name is {2},your name is {1}，'.format('yuming','xixi','tt')
print(str3)


print('-------补齐{:n}--字符串默认左对齐，数字默认右对齐----')
str4 = 'my name is {:10},your name is {:6}，age is {:10}'.format('yuming','xixi',22)
print(str4)

print('--------左对齐{:<n}， 右对齐{:>n} , 居中对齐{:^n}------')
str5 = 'my name is {:>10},your name is {:>6}，age is {:<10}'.format('yuming','xixi',30)
print(str5)

print('-----更简便的写法------')
name1 = 'shen'
name2 = 'zheng'
age = 18
str6 = f'my name id {name1:10},your name is {name2},age is {age:10}'
print(str6)
str7 = f'my name id {name1:>10},your name is {name2:<6},age is {age:<20},'
print(str7)



'''
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格） 
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green          :21;
Mike Mos            :09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''

input = input('请输入： ')
studentstr = input.split(';')   ##将每队信息以分号分割
print(studentstr)   #['Jack Green ,   21  ', '  Mike Mos, 9', '']
for one in studentstr:
    if one !='':      ##只处理非空的值
        name = one.split(',')[0]
        age = one.split(',')[1]
        name = name.strip()
        age = age.strip()
        # print(name,age)
        print(f'{name:<20}:{age:>02};')


# inputStr = input('Please input student age info:')
# studentInfo = inputStr.split(';')
# for one in studentInfo:
#     if ',' not in one:
#         continue
#     name, age = one.split(',')
#     name = name.strip()
#     age = age.strip()
#     if not age.isdigit():
#         continue
#     age = int(age)
#     print('%-20s :  %02d' % (name, age))
