
filepath = f'/Users/shenyuming/Downloads/sym/tuwen/sanguo.txt'
# fp = open(filepath,mode='r')
# ff = fp.read()
# print(ff)
# fp.close()

##  w+ 打开一个文件读写，文件存在从头开始编写，清空写入，文件不存在创建新的
##  r+ 打开一个文件用于读写，从头开始编写，覆盖写入
##  a+ 打开一个文件用于读写，文件存在，从内容末尾开始追加写入，文件不存在创建文件

# fw = open(filepath,mode='w+',encoding='gbk')
# fw.write('汉字dlllsdlsldlsdlsdsdd')
# fw.seek(2)  ##光标回到首位， 数字控制回到首位后，偏移多少位， 汉字两个字节，字母一个字节
# print(fw.read())
# fw.close()


fw = open(filepath,mode='r')
print(fw.readline())     ##读取一行
print(fw.readlines())    ##读取全部返回list
print(fw.readlines()[1])   ##读取全部列表的第二行
print(fw.read().splitlines())   ###读取所有内容,返回list 不带\n

fw.close()

print('@@@@@@@@@@@@@@@@@@2')



# with open(filepath) as file2:
#     print(file2.read().splitlines())


###with open 可以同时操作多个文件，
filepath2 = f'/Users/shenyuming/Downloads/sym/tuwen/xinjian.txt'
with open(filepath) as file3,open(filepath2,'w+') as file5:
    print(file3.read().splitlines())
    file5.write('这是w+新建的文件新写的内容')


##生成测试数据
with open(f'/Users/shenyuming/Downloads/sym/tuwen/xingneng.txt',mode='w+') as file6:
    for i in range(1,10001):
        file6.write(f'zj{i:03},123456\n')