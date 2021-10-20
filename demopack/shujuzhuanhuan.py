import json
##字符串转换为数字
strs = "123456"
sun = []
for i in range(1,len(strs)):
    sun.append(int(i))
print(sun)


##字符串转数字
sd = ['1','3','5']
sdd = []
for f in sd:
    sdd.append(int(f))
print(sdd)


##字符串转列表  ,以逗号分割
b = "dsjf,kfjdfjk,shen"
bb = b.split(',')
print(bb)

bv = "['d','d','s']"
vv = eval(bv)
print(vv)

##每个字符转成列表中的值
j = 'abc'
jj = list(j)
print(jj)

##字符串按分割成列表
po = "shen#da#xian"
pp = po.split('#')
print(pp)


##列表数字 转字符串
a = [1,3,5,7,9]
s = ''
for sf in a:
    s = s+str(sf)
print(s)


##列表转字符串
a = ['hjkl','xccxv']
aa = ' '.join(a)
print(aa)

lie = ["shen","yu","ming"]
l = ','.join(lie)
print(l)


##列表转字典
b = ['d','2','6']
d = ['zhi','value','ok']
bd = dict(zip(b,d))
print(bd)


hh = [['w','d'],['vb','bn'],['ed','fu']]
h = dict(hh)
print(h)

#合并
d = [[1,2.3],[5,6,7],[8,9,0]]
l = sum(d,[])
lists = list(l)
print(lists)


##字典key和value转列表
d = {'x':1,"n":2}
d_key = d.keys()
d_values = d.values()
print(list(d_key))
print(list(d_values))

##取出字典的键值，items()
for L,V in d.items():
    print(f'k:{L},v:{V}')


##字典转字符串
dic = {"s":"ss","f":"ff","v":"vv"}
dc = json.dumps(dic)
print(dc)

#强转成字符串
dd = {"df":"fg","gh":"hj"}
dc = str(dd)
print(dc)

##字符串转字典
zifu = '{"sx":"cv","vb":"bn"}'
iu = json.loads(zifu)
print(iu)

##强转
z = eval(zifu)
print(z)


##全部转为字符串
ll = ['1',3,'r',2]
print([str(i) for i in ll])


##z字符串反转
w = "qwertYhu"
s = w[::-1]
print(s)

l = list(w)
l.reverse()
print(l)

print(w.upper())
print(w.lower())
print(w.capitalize())
print(w.title())


##遍历字典
members = {
    'account1' : 13,
    'account2' : 12,
    'account3' : 15,
}

for account,level in members.items():
    print (f'account:{account}, level:{level}')

##合并字典
another =  {
    'account4' : 13,
    'account5' : 12,
    'account5' : 19,
}
members.update(another)
print(members)

##lisr的sort对原列表排序
aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook'];
aList.sort()
print("List : ", aList)
##reverse=false升序
aList.sort(reverse=False)
print("List : ", aList)

