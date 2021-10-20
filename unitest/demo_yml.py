import yaml

##yml有三种格式，普通格式，字典格式，列表格式

file = open('aa.yml','r' ,encoding='utf-8')
res = yaml.load(file,Loader=yaml.FullLoader)
print(res)

