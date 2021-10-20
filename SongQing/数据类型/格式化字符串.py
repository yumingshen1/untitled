
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

print('-----%ns补位右对齐----字符串本身超过n位，则显示全部字符串--')
print('我是%7s,你是%3s，他是%5s，今年是%10d年，'%('张xx','陈','也不知道是谁',202110))

print('------%-ns左对齐------')
print('我是%-4s,你是%-3s，他是%-5s，今年是%-8d年'%('张xx','陈','也不知道是谁',202110))

print('------%f浮点型，默认保留6位数----')
number = '您输入的数字是：%f'%(3.7)
print(number)
number2 = '您输入的数字是：%.2f'%(3.7) + "保留两位小数"
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
str6 = f'my name id {name1:10},your name is {name2},age is {age}'
print(str6)
str7 = f'my name id {name1:>10},your name is {name2:<6},age is {age:<20},'
print(str7)
