#-*- codeing = utf-8 -*-
#@Time : 2021/5/25 上午11:36
#@Author : yuming shen
#@File : filetest.py
#@Software :PyCharm

# open 'w' 写入模式，打开的文件不存在，就写入一个文件
'''
f = open("test.txt","w")
f.write(r"w=写入, r=只读 默认模式 文件的操作 学习文件的输入读取")
f.close() # 关闭文件
'''

'''
##打开已有文件，追加内容 传入'a'
with open("test.txt",'a')as f:
    f.write(r"此条记录是追加的内容，细心查看下")
'''

#读取文件：
'''
ff = open("test.txt","r")
con = ff.readlines()  # 读取全部数据为列表。
#print(con)
i=1
for temp in con:    #循环读取每一行
    print("%d:%s"%(i,temp))
    i+=1
ff.close()
'''

'''
f = open("test.txt","r")
con = f.readline()   # 只读取一行
print("1:%s"%con)
f.close()
'''

'''
##使用with语句 相当于使用 try...finally，抛出异常，不必写close()
with open("test.txt","r")as f:
    con = f.readlines()
    i = 1
    for temp in con:
        print("%d:%s"%(i,temp))
        i+=1
'''

##os模块对文件的操作
'''
import os
os.rename("test.txt","text1.txt")  #修改文件名字
'''

##try....finally
'''
import time
try:
    f = open("text1.txt",'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("异常。。。")
'''

def writfile():
    with open ("gushi.txt",'w')as f:
        f.write("这是一首古诗，会被复制到另一个文件")


def readfile():
    with open("copy.txt",'r')as f:
        pass




if __name__ == '__main__':
    writfile()
