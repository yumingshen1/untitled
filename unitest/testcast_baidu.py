import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt,data,unpack,file_data
import yaml
from HTMLTestRunner import HTMLTestRunner


#获取数据
def resdfile():
    params = []
    file = open('params.txt','r',encoding='utf8')
    for line in file.readlines():
        params.append(line.strip('\n').split(',')) ##strip('\n')是将数据后的回车去掉，然后以逗号分割数据
    return params


@ddt
class testcase_baidu(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(r"/Users/shenyuming/Downloads/webdriver/chromedriver")
        # self.driver.get("http://www.baidu.com")
        # sleep(3)
        # self.driver.find_element_by_name('wd').clear()
        print("kaishi")

    def tearDown(self):
        # sleep(2)
        # self.driver.quit()
        print("jiehsu")


    # @data(*resdfile())
    # @unpack
    # def test_baiduselect(self,txt):
    #     self.driver.find_element_by_name('wd').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()
    #     sleep(2)
    #     title = self.driver.title
    #     self.assertIn('百度搜索',title)


    # ##简单实现，单个直接传参数
    # @data('数据1','数据2')  ##多个参数的写法，参数之间用逗号
    # def test_01(self,txt):
    #     print(txt)
    # #     print("=======")
    #
    #
    # ##简单实现，直接传多个参数
    # @data(('数据1','数据2'),('资源1','资源2'))  ##多个参数的写法，参数之间用逗号
    # @unpack                         ##多个参数需要用unpack来解包参数才可以，
    # def test_01(self,txt,name):
    #     print(txt)
    #     print(name)
    #     print("=======")


    ##简单实现，文件读取  ，===============    一个*是元祖，两个**是字典
    @data(*resdfile())  ##读取 .txt文件形式 实现, 组件安顺序给值，顺序不要乱
    @unpack  ##多个参数需要用unpack来解包参数才可以，
    def test_01(self, txt, name):
        print(txt)
        print(name)
        print(",,,,,,,")



    #file_data直接操作文件 ，只能识别.yml格式文件，需要导入pyyaml
    @file_data('ppp.yml')
    def test_02(self, txt):
        print(txt)
        print("=======")


    # ##  file_data 使用参数化 只能识别.yml格式文件 ，   ------------------- 断言
    @file_data('qqq.yml')  ##file_data直接操作文件
    def test_03(self, **kwargs):   ## **kwargs以字典格式传入数据不论数量
        name = kwargs.get('name')
        print(name)
        #断言
        self.assertEqual('name',kwargs.get('name'),msg='不匹配')
        taxt = (kwargs.get('taxt'))
        print(taxt)
        print("=======")


    @file_data('www.yml')  ##file_data直接操作文件
    def test_04(self, **kwargs):  ##  **kwargs以字典格式传入数据不论数量
        detail = kwargs.get('detail', '没写用例描述')
        self._testMethodDoc = detail  # 动态的用例描述
        url = kwargs.get('url')  # url
        method = kwargs.get('method', 'get')  # 请求方式
        data = kwargs.get('data')  # 请求参数
        nn = data['username']
        cookieType = kwargs.get('cookieType')
        check = kwargs.get('check')
        cc = check[0]
        dataType = kwargs.get('dataType')
        method = method.lower()  # 便于处理
        print(detail)
        print(url)
        print(method)
        print(data)
        print(cookieType)
        print(check)
        print(dataType)
        print(nn)
        print(cc)



    ###unittest的skip用法：：：：
    # 在用例下加注释是为了在生成报告的时候显示
    ###无条件条跳过
    @unittest.skip('无条件跳过')
    def test_5(self):
        '''用例1'''
        print('1')

    #有条件判断是否跳过
    #@unittest.skipIf(1 < 2, '满足true条件跳过')
    def test_6(self):
        '''用例2'''
        print('2')

    #有条件判断是否跳过
    #@unittest.skipUnless(1 > 2,'满足fail条件跳过')
    def test_7(self):
        print('3')

    #运行失败后不计入失败的case中
    #@unittest.expectedFailure
    def test_8(self):
        print('4')
        #self.assertEqual(1,2,msg='错误不计入失败的case')

    def test_9(self):
        print('5')




if __name__ == '__main__':
    unittest.main()
##main中不能用runner，  因为main中默认使用unittest.main()执行，要是用runner.texttestrunner需要新建.py来调用

