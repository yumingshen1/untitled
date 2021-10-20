##True , Flase
## = 赋值   == 判断是否相等   ！= 判断不相等
##优先级   not > and >or

print('a'=='A')  #ASCII 比较，  一般小写的值大于大写的值
print('a'>'A')

##字符串的比较，只比较第一位，第一位相同时，再比较第二位
print('aA'>'Aa')

list1 = [100,200,232,300,[201,303,505],309]
print(100 in list1)
print(201 in list1[4])
print(201 in list1[-2])

print('----')

##组合条件，not > and >or
print(3>2 and 1<2 or 3==2)
print(1>2 and 2>3 and not True or 3>2)