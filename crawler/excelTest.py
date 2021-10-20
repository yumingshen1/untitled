#-*- codeing = utf-8 -*-
#@Time : 2021/5/29 上午11:11
#@Author : yuming shen
#@File : excelTest.py
#@Software :PyCharm


import xlwt
# workbook = xlwt.Workbook(encoding='utf-8') #创建workbook对象
# worksheet = workbook.add_sheet("sheet1") #创建工作表
# worksheet.write(0,0,"查u你更加爱你")
# workbook.save("student.xls")

workbook = xlwt.Workbook(encoding='utf-8') #创建workbook对象
worksheet = workbook.add_sheet("sheet1") #创建工作表
for i in range(0,10):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save("student.xls")