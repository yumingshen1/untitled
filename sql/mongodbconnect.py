# -*- coding:utf-8 -*-
# @Time : 2022/7/15 12:22
# Auther : shenyuming
# @File : mongodbconnect.py
# @Software : PyCharm

import pymongo

class MongoDBConnect:
    def __init__(self,ip='127.0.0.1',user='admin',password='pass',port=27017):
        self.client = pymongo.MongoClient(f'monogdb://{user}:{password}@{ip}:{port}')
        self.db = self.client['数据库']
    
    #增加
    def insert(self,collection,query,many=False):
        res_set = self.db[collection]
        if many == False:
            res_set.insert_one(query)
        else:
            res_set.delete_many(query)

    ##查询
    def query(self,collection,query,many=True):
        res_set = self.db[collection]
        if many:
            res = res_set.find(query)
            for i in res:
                return i
           # return [one for one in res_set.find(query)]
        else:
            res_set.find_one(query)


    #更新
    def update(self,collection,mydic,newvalues,many=False):
        res_set = self.db[collection]
        if many == False:
            res_set.update_one(mydic, {"$set":newvalues})
        else:
            res_set.update_many(mydic,{'$set':newvalues})

    ##删除
    def delete(self,collection,mydic,many=False):
        res_set = self.db[collection]
        if many == False:
            res_set.find_one(mydic)
        else:
            res_set.delete_many(mydic)

