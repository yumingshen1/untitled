# a = int(input('请输入数值：'))   ##input从键盘接收到的值是字符串，需要转换int
# if a == 1:
#     print('对的')               ##if 和 elif 都是需要写条件的
# elif 2 < a < 10:
#     print('不对么？')
# else:
#     print('啥情况')


# a = input('请输入数值：')
# if not a.isdigit():         #isdigit() ---- > 判断输入的字符串值是不是数字类型，
#     print('您输入的不是纯数字')
# else:
#     a = int(a)             ##将输入的值转换成int类型去判断
#     if a == 1:
#         print('对的')
#     elif 2 < a < 10:
#         print('不对么？')
#     else:
#         print('啥情况')


# age = input('请输入年龄：')
# sex = input('请输入性别：')
# if not age.isdigit():
#     print("您输入的年龄不是数值型")
# elif '\u4e00' <= sex <= '\u9fa5':
#     age = int(age)
#     if age > 3 and sex == '男':
#         print('三岁以上的小男孩')
#     elif age == 2 and sex == '男':
#         print('7岁的小男孩')
#     elif age > 3 and sex == '女':
#         print('三岁以上的小女孩')
#     else:
#         print('未知的')
# else:
#     print('您输入的性别不是汉字')


# a = input('请输入：')
# if not a.isdigit():
#     print('你输入的不是数字')
# else:
#     a = int(a)
#     if a == 0 :
#         print('他是大于0的')
#     elif 8 > a > 3:
#         print('他是有区间得')
#     else:
#         print('不在范围内')


# words = ['高的','矮的','胖的','瘦的','朋友']
# for i in range(5):
#     print('请根据提示输入英文单词：')
#     while(1):
#         word = input(words[i]+':')
#         if word in ('tall','short','fat','thin','friend'):
#             if (word=='friend'):
#                 print('答对了')
#             else:
#                 print('下一题')
#             break
#         else:
#             print('重新输入')


'''
用户从控制台输入一个手机号，判断出运营商(移动（假设号段是130-150）、联通（假设是151-170）、
电信（假设是171-199）),如果用户输入的位数不对，提示用户位数有误;如果用户输入非数字，提示有非法字符
'''

numbs = input('请输入手机号：')
if not numbs.isdigit():
    print("您输入的不是数字")
elif len(numbs)!=11:
    print("您输入的位数不对")
else:
    numbs = int(numbs[0:3])  ###用切片方式获得数据的前三位
    if 130 <= numbs <= 150:
        print("移动运营商")
    elif 151 <= numbs <= 170:
        print("联通运营商")
    elif 171 <= numbs <= 199:
        print("电信运营商")
    else:
        print("不属于任何运营商")