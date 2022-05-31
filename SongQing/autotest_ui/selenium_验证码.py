# -*- coding:utf-8 -*-
# @Time : 2022/5/18 15:16
# Auther : shenyuming
# @File : selenium_验证码.py
# @Software : PyCharm
'''
知识点:  screenshot_as_png  保存元素的截图 ， ddddocr验证码识别
'''
from selenium import webdriver
from time import sleep
import ddddocr

driver = webdriver.Chrome()
driver.get('http://121.41.14.39:8088/index.html')
sleep(2)
driver.find_element_by_css_selector('#username').send_keys('sq2')
driver.find_element_by_css_selector('#password').send_keys('123')
# 获得验证码图片
ele_img = driver.find_element_by_css_selector('img')
## 可以保存图片
# with open('ocr.img','wb') as f:
#     f.write(ele_img.screenshot_as_png)  # screenshot_as_png  bytes类型， 可以保存图片

## 直接获得img的文本 , 导入ddddcor，实例化ddddocr
ocr = ddddocr.DdddOcr()
text = ocr.classification(ele_img.screenshot_as_png)
## 输入验证码
driver.find_element_by_css_selector('#code').send_keys(text)

driver.find_element_by_css_selector('#submitButton').click()

sleep(1)
driver.quit()