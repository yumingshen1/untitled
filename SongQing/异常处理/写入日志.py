'''
logging模块 ， 可以和try 配合写入
'''
import logging
import time
import traceback

##logging先准备好写入的日志级别和路径
# logging.basicConfig(level='INFO',filename=f'/Users/shenyuming/Downloads/sym/tuwen/long3.log',filemode='a+')
# logging.info('info级别的问题')
#
# try:
#     inp = int(input('请输入：'))
#     print(1/inp)
# except:                                                     ##traceback.format_exc()，表示将原格式错误 输出
#     logging.error(time.strftime('%Y-%m-%d %H:%M:%S')+traceback.format_exc())
#

'''
loguru---> logger   颜色区分
'''
import os
from loguru import logger
logger.error('error错误')
logger.critical('critical错误')

if not os.path.exists(f'/Users/shenyuming/Downloads/sym/tuwen/'):
    os.mkdir(f'/Users/shenyuming/Downloads/sym/tuwen/')

logfile = f'/Users/shenyuming/Downloads/sym/tuwen/long5.log'    ##存储路径
logger.add(logfile,rotation='200KB',compression='zip')     ##将日志写入文件 , 每200kb为一个文件， 压缩成zip格式
for i in range(10):
    logger.error('456')


def fun(a,b):
    return a/b

try:
    fun(3,0)
except:
    logger.error('e')