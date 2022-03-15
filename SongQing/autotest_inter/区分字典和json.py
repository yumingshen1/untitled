"""
控制台里面怎么区分是字典还是json字符串：
    1- 单引号是字典
    2- 双引号是json字符串

    dict1 = {"a":"100"}
    print(dict1)
    print(type(dict1))

    #json
    str1 = '{"a":"100"}'
    print(str1)
    print(type(str1))

json与字典的区别  {}  "" none
    # dict1 = {"a":False}
    # print(dict1)
    # print(type(dict1))
    # #字典变成json 类型
    # print(json.dumps(dict1))
    #
    #json 类型 转字典 json.loads()
"""
dict1 = {'a':'100','b':'200'}
print('dict1类型---》',type(dict1))

dict2 = {"a":'100',"b":'200'}
print('dict2类型---》',type(dict2))

dict3 = '{"a":"we","b":"xc"}'
print(dict3)
print('dict3的类型---》',type(dict3))

dict4 = "{'a':'we','b':'xc}"
print('dict4的类型----》',type(dict4))

dict1 = {"a": "100"}
print(dict1)
print(type(dict1))

# json
str1 = '{"a":"100"}'
print(str1)
print(type(str1))

str2 = '''{'a':'100'}'''
print(str2)
print(type(str2))