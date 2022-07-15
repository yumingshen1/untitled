# -*- coding:utf-8 -*-
# @Time : 2022/7/15 11:52
# Auther : shenyuming
# @File : test_mongodb.py
# @Software : PyCharm
import pymongo

##创建
client = pymongo.MongoClient("mongodb://user:password@ip:port")
#指定数据库
db = client['数据库']
#在指定集合（表）
collection = db['表']

#增加一条数据
collection.insert_one({"键":'值',"键":'值',"键":'值'})

##增加多条语句
mydic = [{"键":'值',"键":'值',"键":'值'},{"键":'值',"键":'值',"键":'值'}]
collection.insert_many(mydic)


##查询
myquery = {"键":"值"}
collection.find_one(myquery)
collection.find(myquery)

#修改
myquery = {"键":"值"}
newvalues = {"$set":{"键":"新值"}}
collection.update_one(myquery,newvalues)
collection.update_many(myquery,newvalues)

##删除
mydic = {"键":"值"}
collection.delete_one(mydic)

mydic = {"键":{"$regex":"^值"}}  ##删除所有已值开头的数据
collection.delete_many(mydic)


