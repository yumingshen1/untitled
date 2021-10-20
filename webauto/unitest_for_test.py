import unittest
from time import sleep
from ddt import ddt,file_data,unpack,data
from selenium import webdriver
import yaml

##文件读取
def resf_file():
    file = open('paramx.txt','r',encoding='utf-8')
    list = []
    for i in file.readlines():
        list.append(i.strip('\n').split(','))
    file.close()
    return list

##读取yaml文件 -  file_data不需要在读取
def read_yaml():
    file = open('testt_yaml.yaml', encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)


@ddt
class CeshiUnitest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r'/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
        self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    #使用 读取文件形式传入参数
    # @data(*resf_file())
    # @unpack
    # def test_1(self,name,password):
    #     self.driver.find_element_by_name('accounts').send_keys(name)
    #     self.driver.find_element_by_name('pwd').send_keys(password)
    #     self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
    #     sleep(2)


    #使用 yaml文件形式传入参数
    @file_data('testt_yaml.yaml')
    def test_1(self,**user):
        self.driver.find_element_by_name('accounts').send_keys(user.get('name'))
        self.driver.find_element_by_name('pwd').send_keys(user.get('psw'))
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main
