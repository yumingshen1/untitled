# -*- coding:utf-8 -*-
# @Time : 2022/7/15 11:16
# Auther : shenyuming
# @File : mysqlconnect.py
# @Software : PyCharm

import pymysql

class DBConnect:
    def __init__(self,host='127.0.0.1',port=3306,user='root',password='Sym123456',database='ceshi'):
        self.db = pymysql.connect(host=host,port=port,user=user,password=password,database=database)
        self.cursor = self.db.cursor()

    ##查询
    def select(self,sql,many=True):
        self.cursor.execute(sql)
        if many:
            result = self.cursor.fetchone()
        else:
            result = self.cursor.fetchall()
        return result

    ## 通用操作
    def do(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as error:
            self.db.rollback()
            print(f'mysqldb error {error}')
            raise error
        self.db.commit()


    def insert(self,sql):
        self.do(sql)

    def delete(self,sql):
        self.do(sql)

    def update(self,sql):
        self.do(sql)


    def exit(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    db = DBConnect()
    sql = 'select * from biaodan'
    res = db.select(sql)
    print(res)
    db.exit()