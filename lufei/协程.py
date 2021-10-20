#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午3:13
#@Author : yuming shen
#@File : 协程.py
#@Software :PyCharm

import asyncio  #协程

#被async修饰的方法需要挂起，调用后返回一个协程对象将其加入到事件中
async def request(url):
    print('正在请求url',url)
    print('请求成功',url)
    return url #如果调用了回调函数，此返回值就是回调函数的返回值
c = request('www.sougou.com')

#创建一个事件循环对象
# loop = asyncio.get_event_loop()
# #将协程对象加入到事件循环中，然后启动
# loop.run_until_complete(c)

# task的使用
# loop = asyncio.get_event_loop()
# #基于事件循环对象loop创建一个task对象
# task = loop.create_task(c)
# loop.run_until_complete(task)

# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# loop.run_until_complete(task)

def callback_func(task):
    #result返回的就是任务对象中封装的协程的对象对应的函数返回值
    print(task.result())

#回调函数
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# #将回调函数绑定到任务对象
# task.add_done_callback(callback_func)
# loop.run_until_complete(task)

loop = asyncio.get_event_loop()
task = loop.create_task(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)
