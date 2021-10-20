#-*- codeing = utf-8 -*-
#@Time : 2021/6/8 下午2:53
#@Author : yuming shen
#@File : sqlitText.py
#@Software :PyCharm

import sqlite3
conn = sqlite3.connect("test.db") #打开或创建数据文件
c = conn.cursor() # 游标
sql = '''
    create table company
        (id int  primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real
        )
'''
sql1 = '''
    insert into company(id,name,age,address,salary)
    values(1,'账单',20,"成都",500000)

'''
# c.execute(sql)
# c.execute(sql1)  #执行sql
# conn.commit()   #连接上提交
# conn.close()    #连接上关闭
# print("建表成功")


sql2 = '''
    select * from company
'''
cur = c.execute(sql2)  #执行sql
for i in cur:
    print("id = ", i[0])
    print("name = ", i[1])
    print("age = ", i[2])
    print("address = ", i[3])
    print("salary = ", i[4])
conn.close()    #连接上关闭

