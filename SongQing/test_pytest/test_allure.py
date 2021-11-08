
import pytest
import allure
import os

# def test_01():
#     print('开始')
#     assert 1==1
# def test_02():
#     print('开始')
#     assert 1==1



'''
 setup_method(self): \ teardown_method(self): 类中的每条用例执行前后都会执行
'''
# class Test1:
#     def setup_method(self):
#         print('开始')
#     def test_01(self):
#         assert 1==2
#     def test_02(self):
#         assert 1==3
#     def test_03(self):
#         assert 3== 3
#     def teardown_method(self):
#         print('JIEHSU')
#

'''
setup_class(self):
teardown_class(self):
类中所有的用例执行前后，只执行一次开始结束
'''
#
# class Test2:
#     def setup_class(self):
#         print('开始')
#     def test_01(self):
#         assert 10==10
#     def test_02(self):
#         assert 12==30
#     def test_03(self):
#         assert 22== 100
#     def teardown_class(self):
#         print('JIEHSU')

'''
将 setup 、 teardown 放到class的外面， 利用于可以用也可以不用
'''
#
# # @pytest.fixture()             ## 装饰器 @pytest.fixture(参数) 默认参数==>scope = method , 可以带有class moudle  session
# @pytest.fixture(scope='class')
# def fun1():                     ## 被@pytest.fixture()装饰 代表内容是 setup
#     print('开始的')
#     yield                  ## yield 代表后面的内容是 teardown
#     print('JIESHU')
#
# class Test3:
#     def test_data_01(self,fun1):
#         assert 1==0
#     def test_data_02(self,fun1):
#         assert 1==1


'''
参数化  
'''
# class Test5:
#     @pytest.mark.parametrize('real,result',[[1,2],[2,2],[2,3]])
#     def test_5(self,real,result):
#         assert real==result

# class Test6:
#     @pytest.mark.parametrize('real,result',[(1,1),(0,1),(100,1)])
#     def test_6(self,real,result):
#         assert real==result


# class Test7:
#     @pytest.mark.parametrize('real,result',([1,1],[1,3],[0,-1]))
#     def test_7(self,real,result):
#         assert real==result


# class Test8:
#     @pytest.mark.parametrize('real,result',((1,1),(1,0)))
#     def test_8(self,real,result):
#         assert real==result
#


list1 = [[20,20],[10,10],[15,16]]
@allure.feature('层级1')
@allure.story('层级2')
@allure.title('层级3')
class Test9:
    @pytest.mark.parametrize('real,result',list1)
    def test_9(self,real,result):
        assert real==result


if __name__ == '__main__':
    pytest.main(['test_allure.py','-s','--alluredir','./report'])  ## -s 表示打印print
    os.system('allure generate ./report -o ./report/report --clean')

