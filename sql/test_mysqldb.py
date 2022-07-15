import pymysql

#数据库连接
con = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Sym123456',
    database='ceshi',
    port=3306)

#创建游标
c = con.cursor()
c.execute('select * from biaodan')

# row = c.fetchone()
# print("取出一条数据：", row)

# rows = c.fetchmany(10)
# print("取出10条数据:" + rows)

rr = c.fetchall()
print("取出所有数据：",rr)

##创建表sites
#c.execute("CREATE table sites (name VARCHAR(255),url VARCHAR(255))")
#添加主键
#c.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

##展示库的所有表
# c.execute("SHOW TABLES")
# for x in c:
#     print(x)

##删除，为了防止sql注入，使用%s占位符转译语句
# sql = "DELETE from biaodan where classname = %s"
# na = ("留学生14")
# c.execute(sql,na)
# con.commit()

#c插入数据
# for x in range(20): ##循环添加数据，f是python字符串格式化，{x+1}是填入变量
#     c.execute(f"insert into biaodan(name,age,classname,school,city,county) values ('辰{x+1}',25,'留学生1{x+1}','北大','北京','China')")
#
# ##变动数据库信息的都需要 con.commit()
# con.commit()

# ##循环取出所有数据,range内置函数，rowcount循环每一条
# for i in range(c.rowcount):
#     i = c.fetchone()
#     print(i)

##修改
# c.execute("Update biaodan set classname = '修改数据' where id = 70")
# con.commit()

con.close()


