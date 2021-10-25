'''

包与模块
'''

##下载包慢时可以用国内镜像
##豆瓣源 : pip install 包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
##清华源：pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn


import sys
for one in sys.path:   ###显示python的标准路径
    print(one)
    ##标准路径中第一个是当前路径，第二个是工程路径，后面的都是标准路径
sys.path.append('路径') ##将路径添加到标准路径中
##永久添加标准路径，进入site-packages目录，新建一个.pth文件， 文件名不限，以.pth为后缀，在文件中写入地址，


'''
yaml文件读取
'''


###读取 同一类型数据
import yaml
# with open('config.yaml') as f:
#     con = yaml.load(f,Loader = yaml.FullLoader)
#     print(con)
#

##读取多种类型的数据
with open('config.yaml') as f1:
    conn = yaml.load_all(f1,Loader=yaml.FullLoader)
    for one in conn:
        print(one)

