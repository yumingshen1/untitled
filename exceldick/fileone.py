import openpyxl
import xlrd
from xlutils.copy import copy

#打开excel
wordbook = xlrd.open_workbook('examples.xlsx')
#复制表格,在sheet中写入数据
data_copy = copy(wordbook)
sheet_copy = data_copy.get_sheet('Sheet1')

try:
    sh = wordbook.sheet_by_name('Sheet3')
except:
    print('no 工作表1 in %s named 工作表1',format('examples.xlsx'))

#行数
nrows = sh.nrows
#列数
ncols = sh.ncols

print('行{0},列{1}'.format(nrows,ncols))

##循环遍历加入数组中
row_list = []
for i in range(1,nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)

print(row_list)


#将数组处理,每组数据分开
datas = []
for lists in row_list:
    data = (",").join('%s' % id for id in lists) #提示ypeError: sequence item 0: expected str instance, float found出现浮点数，将list转换成string
    datas.append(data)

print(datas)

# wb = openpyxl.load_workbook('examples.xlsx')
# print(wb.sheetnames)#获取所有表格
# sheet = wb['Sheet3']#根据sheet名字获取数据
# print(sheet.title)
# print(sheet['A2'].value) ##获得指定表格内容
#
