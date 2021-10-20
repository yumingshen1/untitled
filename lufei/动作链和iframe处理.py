#-*- codeing = utf-8 -*-
#@Time : 2021/7/19 下午2:20
#@Author : yuming shen
#@File : 动作链和iframe处理.py
#@Software :PyCharm
from selenium import  webdriver
from selenium.webdriver import ActionChains
from time import sleep
bro = webdriver.Chrome(executable_path='/Users/shenyuming/Downloads/sym/xiazai/webdriver/chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
##进入iframe操作
bro.switch_to.frame('iframeResult')
#操作元素
div= bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)
#点击元素并长按
action.click_and_hold(div)
for i in range(5):
    #移动鼠标到指定位置
    action.move_by_offset(17,0).perform()
    slice(0.3)
#释放动作链
action.release()
sleep(5)
bro.quit()