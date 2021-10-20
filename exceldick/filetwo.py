import xlrd
import requests
import json
from xlutils.copy import copy

execdir=r"/Users/shenyuming/Downloads/examples.xlsx"

workbook = xlrd.open_workbook(execdir)

print(workbook.sheet_names())

worksheet = workbook.sheet_by_name('Sheet3')

##取指定单元格
cell_vall = worksheet.cell(2,3).value
print(cell_vall)

row = worksheet.row_values(1)
col = worksheet.col_values(1)
print(row)
print(col)

#总行数
nrows = worksheet.nrows
#总列数
ncols = worksheet.ncols

#将数据带入数组
list_data = []
for i in range(1,nrows):
    list = worksheet.row_values(i)
    list_data.append(list)
print(list_data)

##处理数组将每个数据分割
row_data = []
for data in list_data:
   datas =  (",").join(data)
   row_data.append(datas)
print(row_data)

##登录接口
token_url = "http://47.96.181.17:9090/rest/toController"
data = {"userName":"J201903070064","password":"362387359"}
headers = {"Content-Type":"application/json"}
resp = requests.post(token_url,data=json.dumps(data),headers=headers)
token = resp.json()['token']
print(token)


##添加用户
for d in row_data:
    addurl = 'http://47.96.181.17:9090/rest/ac01Controller'
    adduserdata = json.loads(d)
    adduserheard = {"Content-Type":"application/json","X-AUTH-TOKEN":token}
    adduser_resp = requests.post(addurl,data=json.dumps(adduserdata),heard=adduserheard)
print(adduser_resp.text)

#复制excel
workbookwr = copy(workbook)
wrsheet = workbookwr.get_sheet()

##f复制excel 写入结果
temp = 1
for i in list_data:
    res = adduser_resp.json()['message']
    if res == '成功':
        print('----')
        excel_res = 'succes'
        wrsheet.write(temp, 3, excel_res)
        workbookwr.save(r"/Users/shenyuming/Downloads/examples-res.xlsx")
    else:
        print('/////')
        excel_res = 'fail'
        wrsheet.write(temp, 3, excel_res)
        workbookwr.save(r"/Users/shenyuming/Downloads/examples-res.xlsx")
    temp+=1

