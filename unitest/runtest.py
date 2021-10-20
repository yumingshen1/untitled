import unittest,os
from unitest.testcast_baidu import *
from HTMLTestRunner import HTMLTestRunner
import time

##创建一个测试套件
suite = unittest.TestSuite()
#添加测试用例  方式一
# suite.addTest(testcase_baidu('test_2'))
# suite.addTest(testcase_baidu('test_5'))
# suite.addTest(testcase_baidu('test_3'))

##添加测试用例， 方式二  批量添加
# case = [testcase_baidu('test_2'),testcase_baidu('test_5'),testcase_baidu('test_3')]
# suite.addTests(case)

##添加测试用例  方式三， 调用一个类 下所有的用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testcase_baidu))

##通过传入目录，运行该目录下符合文件名的用例
# test_dict = './'
# discovre = unittest.defaultTestLoader.discover(start_dir=test_dict,pattern='test*.py')


##套件通过TextTestRunner的对象来运行
# runner = unittest.TextTestRunner()
# runner.run(suite)


###使用HTMLTestRunner生成报告

report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = '../report/'
report_file = report_path + 'report{}.html'.format(time.strftime("%Y%m%d%H%M%S",time.localtime()))
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file,'wb') as report:
    #执行用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testcase_baidu))

    ##结合HTMLTestRunner报告使用 需要用HTMLTestRunner来运行
    runner = HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)
report.close()

