# -*- coding:utf-8 -*-
# @Time : 2022/5/24 10:26
# Auther : shenyuming
# @File : string_count.py
# @Software : PyCharm

# def counts(str1,str2):
#输入
String_1 = input('SASxza')
String_1.upper() #大写
list_1 = list(String_1)
print('list_1:',list_1)

#查询
check = input('a')
check.upper()
print('check:',check)
num = 0
for word in list_1:
    if word == check:
        num+=1
print(num)

str1 = 'QASDa'
str2 = 'a'
# if __name__ == '__main__':
#     counts(str1, str2)
