#-*- codeing = utf-8 -*-
#@Time : 2021/7/21 下午3:49
#@Author : yuming shen
#@File : 协程-多任务.py
#@Software :PyCharm

import asyncio
import time
 #多任务异步协程

async def request(url):
    print('正在下载',url)
    #异步协程中time.sleep是同步模块相关代码，无法实现异步
    # time.sleep(2)
    #当在asynico遇到阻塞必须手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)

start = time.time()
urls = ['www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com']
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end-start)