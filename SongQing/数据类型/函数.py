def sumdata():
    print("1212")
sumdata()        ##返回的只是函数内的一条语句，
print("----")
print(sumdata())   ##会有返回 none， 因为函数没有返回值

def sumdata2(a,b):   ##函数有两个形参，传入两个值
    return a*b
print(sumdata2(2,3))  ##调用函数，传入两个实参，获得返回值

print("------函数的缺省值-------")
def sumdata2(a=2,b=3):
    return a+b
print(sumdata2())
print(sumdata2(4,5))
print(sumdata2(5,b=7))

print("------函数中可以出现多个return-------")
def sumdata7(n):
    if n > 0:
        return n
        return -n     ##自第一个return之后就已经退出循环，不在执行下一句，不可到达语句。
    else:
        return -n
print(sumdata7(-9))


print("-------一个return返回多个值---------")
def sumdata8(a,b):
    return a+b,a*b,a/b     ##一次返回多个值是返回的一个元祖
print(sumdata8(2,3))

def sumdata8_new(c,d):
    return [c+d,c*d,c-d,c**d]    ##return返回的是一个列表，是一个对象，结果就不会在有元祖形式返回
print(sumdata8_new(3,5))


print("----可变长度参数-----")
def sumdata3(a,*args):
    return (a,a*args)
print(sumdata3(1,2,3,4,5))

def sumdata4(a,*args):
    return (a,*args)         ##俗称解包，少一层元组， 一般低版本中3.7下兼容
print(sumdata4(1,2,3,4,5))

def sumdata5(a,*args):
    return a,args            ##此写法会多一层元祖，
print(sumdata5(1,2,3,4,5))

def sumdata7(*args):
    return args
print(sumdata7(2,5,9))


print('-----关键字参数-----')
def sumdata6(**karags):
    return karags
print(sumdata6(name = '西西',age = 18))


'''
根据身份证号判断其拥有者的性别

'''


# def idcard(num):
#     length = len(num)
#     print("身份证的长度：",length)
#     if len(num) != 18:
#         print('您输入的长度不够！')
#     elif not num[0:16].isdigit():
#         print('您输入的前17位不是数字！')
#     # num = int(num)
#     elif int(num[-2]) % 2 == 0:
#         print('这是女性')
#     else:
#         print('这是男性')

def idcard2(num):
    length = len(num)
    print("身份证的长度：",length)
    if len(num)!=18:
        print("您输入的位数不对")
    elif not num[0:16].isdigit():
        print('您的前17位中有的不是数字')
    elif not num[-1].isdigit() and num[-1] not in ['X','x']:
        print('您的最后一位不符合规则')
    else:
        if int(num[-2]) % 2 ==0:
            print('这是女性')
        elif int(num[-2]) % 2 !=0:
            print('这是男性')
        else:
            print('这是人妖')

nums = '13018519921225181X'
idcard2(nums)


