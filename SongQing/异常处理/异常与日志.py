
##异常是程序中出现错误
## try except语句，至少有一个except，也可以有多个，  也可以有一个else语句，一个finally语句


# try:
#     input = int(input('请输入一个数： '))
#     print(1/input)
# except ZeroDivisionError:       ##非零错误
#     print('请输入正整数')
# except ValueError:              ##非数字错误
#     print('请输入数字')
# except:                         ##捕获任何异常
#     print('程序出错')
# else:                           ##程序没有任何错误执行else
#     print('程序没有出现任何错误，则执行')
# finally:
#     print('无论程序是否出错，都会执行')



'''
常见的异常：
NameError   --> 未定义的变量 
IndexError  -->下表越界
FileNotFoundError  -->找不到文件

所有的异常都属于 Exception的子类，或者子类的类

'''

##假装有异常   rasie
import os

try:
    raise IOError
except:
    print('io异常')

try:
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
except:
    print('不能大于5')
#
# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))



'''
    日志
    logging模块，配合try except 记录日志
'''

import logging      ##  日志
import traceback     ## 用于打印原格式的错误
import time

##  代表将日志写入的级别和目录
logging.basicConfig(level='DEBUG',filename=f'/Users/shenyuming/Downloads/sym/tuwen/long1.log',filemode='a+')

## 如果不加 logging.basicConfig() , 以下直接写会打印在控制台 ，加了logging.basicConfig(输入到文件)   debug info 默认不打印
# logging.debug('debug级别')
# logging.info('info级别')
# logging.warning('warning级别')
# logging.error('error级别')
# logging.critical('崩溃级别')


'''
打印原有的错误到文件，打印时只能用默认的except
'''
#
# try:
#     input = int(input('请输入一个数： '))
#     print(1/input)
# except:       ##打印原有的错误到文件，打印时只能用默认的except，  time.strftime('%Y-%m-%d %H:%M:%S')加入时间
#     logging.error(time.strftime('%Y-%m-%d %H:%M:%S')+traceback.format_exc())




'''
    日志
    logger 模块,    import loguru import logger    ， 颜色区分
'''
import os
from loguru import logger
logger.debug('debug级别')
logger.info('info级别')
logger.warning('waring级别')
logger.error('error级别')
logger.critical('崩溃级别')


if not os.path.exists('/Users/shenyuming/Downloads/sym/tuwen/'):  ##路径不存在则创建
    os.mkdir('/Users/shenyuming/Downloads/sym/tuwen/')

logfile = '/Users/shenyuming/Downloads/sym/tuwen/long2.log'     ##创建文件
logger.add(logfile)                             ##  将日志写入创建好的文件中 ，

for i in range(1000):                           ##写入数据
    # logger.info('试一试')                          ## 先准备好文件路径和文件，然后在写添加进文件，最后在写入数据，顺序不能乱
    logger.exception('zzzz')



def fun(a,b):
    return a/b

try:
    fun(2,0)
except:
    print('cuowu')
    logger.exception('c')