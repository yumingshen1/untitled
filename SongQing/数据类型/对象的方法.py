###方法就是函数，只是写在类里面

str1 = 'qqqwedsxcmkirow'
print('----index() -----  find() ---- ')
print(str1.index('w',5))   ##index()返回字符串中某个或某些字符串在其中的位置,默认从头找，也可以指定位置 ， 找不到会报异常
print(str1.find('q',5))  ## find()和index作用类似，find找不到会返回-1，

str2 = "   jdksjsd89 7plpsd  "
print("----strip()--只能去掉首尾的空格和制定字符----")
print(str2.strip())
str3 = "dsklislakllildd"
print(str3.strip('d'))

print("-----repalce()---返回str型---")
str4="ADEJCMFOOKPPPA"
print(str4.replace('A','1').replace('J','替换'))

print("------startswith()------判断字符串是否以某个或某些字符开头或结尾，返回布尔型")
str5 = "ppLsajinguoren"
if str5.startswith('ppL'):
    print('1')
else:
    print('0')

if str5.endswith('en'):
    print('正确')
else:
    print('再看看')

print("-------split()-----切割字符串，有一个参数，指定以该参数分割-分割的字符在首位会产生一个空值--")
str6 = "qeid,jdpk,asod,096s"
print(str6.split('d'))
print(str6.split('q'))

d = '111'
print(d.isalpha())

dd = '111a'
print(dd.isdigit())

ss = 'my name is jack'
print(ss.split(' ')[-2])

'''
现有一个游戏系统的日志文件，记录内容的字符串 的格式 如下所示
 
A girl come in, the name is Jack, level 955;
 
其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。
 
其它部分可能都是会变化的，比如，可能是下面这些
 
A old lady come in, the name is Mary, level 94454
 
A pretty boy come in, the name is Patrick, level 194
 
请大家实现一个函数，名为getName，如下所示
 
def getName(srcStr):
    函数体
该函数的参数srcStr 是上面所描述的格式字符串（只处理一行），该函数需要将其中的人名获取出来，并返回
 
比如 调用 getName('A old lady come in, the name is Mary, level 94454')
 
返回结果应该是 'Mary'
 
参考答案，往下翻
'''

name = 'A girl come in, the name is Jack, level 955;'

def getName(str):
    return str.split('the name is ')[1].split(',')[0]
print(getName(name))
