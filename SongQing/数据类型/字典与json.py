
###字典是无序的
dictA = {'A':'apple','B':'banana'}
dictB = {'B':'banana','A':'apple'}
print(dictA==dictB)

dictC = [10,20]
dictD = [20,10]
print(dictC==dictD)


##字典的建是唯一的
dictF = {'A':'xxx','A':'yyy'}
print(dictF)

##字典的新增与修改是一样的，根据键修改值，，已有新增，无则增加
dictG = {'A':'apple','B':'banana'}
dictG['A'] = 'origin'
dictG['C'] = 'tomato'
dictG.update({'B':'xigua','E':'chengzi'})  ##一次性修改或增加多个键
print(dictG)

##循环字典
for key in dictG.keys():
    print(key)
for value in dictG.values():
    print(value)
for k,v in dictG.items():
    print(k,v)

##清空字典
# print(dictG)
# dictG.clear()  #清空字典，地址不变
#dictG = {}    ##清空字典，地址也改变，相当于创建新的字典
# print(dictG)


#####json

str1 = '''
{"aaC03":"张三",
"aaC303":"18515607030",
"crm003":"1",
"crm005":"1"
}'''
print(type(str1),'---str---')
print(str1)
##将json格式的字符串转变为字典，修改值，在转为json
import json
from random import randint
str1_new = json.loads(str1)  ##转为字典类型
str1_new['aaC303'] = f'133{randint(10000000,99999999)}'  ##修改字典的值， 使用随机数生成，用字符格式化方式
str1 = json.dumps(str1_new,ensure_ascii=False)  #将修改好的字典在转换为json, ensure_ascii 处理中文编码
print(str1)


