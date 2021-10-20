#-*- codeing = utf-8 -*-
#@Time : 2021/7/14 下午4:56
#@Author : yuming shen
#@File : 线程池.py
#@Software :PyCharm
import time
from multiprocessing.dummy import Pool   #线程池

# def get_page(str):
#     print("正在下载：",str)
#     time.sleep(2)
#     print("下载成功：",str)
# name_list = ['xiaozi','mo','mm','cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%d second'% (end_time-start_time))

#使用线程池异步执行
start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功：",str)
name_list = ['xiaozi','mo','mm','cc']
#实例化线程池对象
pool = Pool(4)
pool.map(get_page,name_list)
end_time = time.time()

print('%d second'% (end_time-start_time))