'''
#思考题讲解1
#第三次课思考题1
#根据身份证号判断拥有者的性别
'''
# inputstr= input('请输入：')
# print('长度：',len(inputstr))
# if len(inputstr) != 18:
#     print('您输入的位数不对')
# elif not inputstr[0:16].isdigit():
#     print('您的前17为不是数字')
# elif not inputstr[-1].isdigit() and inputstr[-1] != 'X':
#     print('您的最后一位规则不对')
# else:
#     if int(inputstr[-2]) % 2==0:
#         print('女性')
#     else:
#         print('男性')




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
'''

srcStr = 'A old lady come in, the name is Mary, level 94454'

##步骤分解：
ss = srcStr.split(' the name is ')[1]
sc = ss.split(',')[0]
# print(ss)
# print(sc)
##函数写入
# def getName(srcStr):
#     ss = srcStr.split(' the name is ')[1].split(',')[0]
#     print(ss)
# getName(srcStr)





# 第四次课思考题1
'''
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格） 
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green          :21;
Mike Mos            :09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''
#
# studentinput = input('请输入信息：')
# one_student = studentinput.split(';')  #分割得到每一个学生,返回的是一个列表
# print(one_student)
# for one in one_student:
#     if one !='':            ##判断不为空的学生信息，进行name和age的获取
#         name = one.split(',')[0].strip()   ##用split()切割方式得到名字，然后用strip()方式去除前后空格
#         age = one.split(',')[1].strip()
#         # print(name,age)
#         print(f'{name:<20}:{age:>02};')   ##使用字符串格式化方式输出信息
#
#


'''
下面的log变量记录了云服务器上 当天上传的文件信息
其中第一列是文件名，第二列是文件大小
请编写一个程序，统计出不同类型的 文件的大小总和
比如：
jpeg  9988999
json   324324
png   2423233
'''
log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0	
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0	
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0	
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0	
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0	
f20180111090619/i_3BKlsRaZ.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156330575626044	image/jpeg	0	
f20180111090619/i_5XboXSKh.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156329453409855	image/jpeg	0	
f20180111090619/i_6DiYSBKp.jpg	74017	FrYG3icChRmFGnWQK6rYxa88KuQI	15156329461803290	image/jpeg	0	
f20180111090619/i_76zaF2IM.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156334738356648	image/jpeg	0	
f20180111090619/i_B6TFYjks.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156329464034474	image/jpeg	0	
f20180111090619/i_N9eITqj3.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156330419595764	image/jpeg	0	
f20180111090619/i_QTSNWmA6.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156333104224056	image/jpeg	0	
f20180111090619/i_XdHcAfh1.jpg	56479	FjLQIQ3GxSEHDfu6tRcMylK1MZ05	15156334227270309	image/jpeg	0	
f20180111090619/i_Xyy723MU.jpg	50076	FsfZpQzqu084RUw5NPYW9-Yfam_R	15156334229987458	image/jpeg	0	
f20180111090619/i_d8Go0EOv.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156334736228515	image/jpeg	0	
f20180111090619/i_diuHmX53.jpg	40591	FuTx1pw4idbKnV5MSvNGxCA5L470	15156333878320713	image/jpeg	0	
f20180111090619/i_qQKzheSH.jpg	55858	Fj0A3i8V7fzzOiPQFL79ao15hkN9	15156329456666591	image/jpeg	0	
f20180111090619/i_rHL5SYk8.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156336509742181	image/jpeg	0	
f20180111090619/i_xZmQxUbz.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156333240603466	image/jpeg	0	
f20180111090619/i_zBDNgXDv.jpeg	73616	FlgNwq8lypgsxrWs_ksrS_x47SQV	15156334232887875	image/jpeg	0	
f20180111090619/j_4mxbEiVh.json	2990	Fpq-3yl3Yr1CadNrJVSDnpeRhQtT	15156331445226898	application/json	0	
f20180111090619/j_i1K74768.json	3042	Fl5PpDw1TsZXMuhoq1RUrOeGZ6br	15156335067090003	application/json	0	
f20180111095839/i_Q7KMKeda.png	518522	Fl-yB1_ruL2uxZN9k7DjB62h9dYH	15156359599713253	image/png	0	
f20180111095839/j_5DpqHolV.json	184	FoYvi7cmSrzuVjUgCRzW5kU95SVo	15156359719719064	application/json	0	
f20180111100442/i_No8kToIV.jpg	48975	Fu1cw3f--5Vpz9kLGeJfvljhCtyZ	15156364349642377	image/jpeg	0	
f20180111100442/i_P1bkvSeg.jpg	68200	FvYe8vi46TjUKhEy_UwDqLhO6ZsW	15156363800690634	image/jpeg	0	
f20180111100442/i_T1AulKcD.jpg	52641	Fj2YzvdC1n_1sF93ZZgrhF3OzOeY	15156364021186365	image/jpeg	0	
f20180111100442/i_X8d8BN07.jpg	50770	FivwidMiHbogw77lqgkIKrgmF3eA	15156363969737156	image/jpeg	0	
f20180111100442/i_g0wtOsCX.jpg	76656	Fmtixx0mP9CAUTNosjLuYQHL6k0P	15156363448222155	image/jpeg	0	
f20180111100442/i_h5OT9324.jpg	72672	FvbIqPLTh2cQHTIBv2akUfahZa_Z	15156364401354652	image/jpeg	0	
f20180111100442/i_he8iLYI6.jpg	49399	FjeJvwjwhU-hKZsq66UoBg9_tEJs	15156363907932480	image/jpeg	0	
f20180111100442/i_kg29t7Pp.jpg	76293	FuYj__sSeEN7AsXMbxO24Z8Suh8d	15156364156384686	image/jpeg	0	
f20180111100442/i_oz1YoBI1.jpg	75620	FkY3xsUMwOI01zgoH1iXXgiQeq6I	15156364089112904	image/jpeg	0	
f20180111100442/i_xrOT98on.jpg	50021	Fql7ookM1Rc6V7VairKAfnKe-o9w	15156363856357316	image/jpeg	0	
f20180111135114/i_Zqt8Tmoe.png	161629	FlELw59_mV3VqDBLyu1BKN4fIWnx	15156500155209863	image/png	0	
f20180111135114/j_uhHoMXKq.json	159	FrypljwAr2LgoLAePBNTUYTUAgDt	15156500200488238	application/json	0	
f20180111142119/i_s83iZ2GR.png	92278	Fns8tdh3JCkRmfE_COYEu4o8w03E	15156517082371259	image/png	0	
f20180111142119/j_0g45JRth.json	159	Fq1rFwdRguYRXrp61nGZ5TsUG1V-	15156517143375596	application/json	0	
f20180111144306/i_yE5TC84E.png	139230	Fjf61ymabEnEvnr5ZMHFjXGCrYlP	15156530038824150	image/png	0	
f20180111144306/j_OF4WVtSH.json	159	FqwkKcxfo8jd0jFUyuH4X2CrnE9q	15156530083419530	application/json	0	
f20180111150230/i_KtnER4g3.png	120044	FuwOWdrqzcr2-UScem-LzEMgMezs	15156541734892258	image/png	0	
f20180111150230/j_xMSUEejY.json	158	FjJr_4deMqFphGaptm-2Pa6wwRP2	15156541771989216	application/json	0	
f20180111151741/i_JuSWztB3.jpg	92506	FrIjRevHSi6xv4-NQa2wrHu5a1zQ	15156550875370965	image/jpeg	0	
f20180111153550/i_9wWzVenl.gif	769872	FvslKY9JUaCQm-lu02E34tvAP_oG	15156561674621628	image/gif	0	
'''
# dict = {}
# line_list = log.split('\n')  #获取每一行，
# for one in line_list:
#     if one !='':           ##只处理非空
#         one1 = one.split('\t')[0]  ##切割获得文件类型的一段
#         # print(one1)
#         file_type = one1.split('.')[1]  ##切割文件类型一段，获得文件类型的后缀
#         file_size = int(one.split('\t')[1])  ##获得文件大小的一段
#         # print(file_size)
#         if file_type not in dict:
#             dict[file_type] = file_size
#         else:
#             dict[file_type]+= file_size
# print(dict)





'''
每一行记录保存了学生的一次签到信息。
每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号('2017-03-13 11:50:09', 271, 131),
要求大家实现下面的函数。其中参数fileName 为 数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：
key 是各个学生的id号， value是 该学生的签到信息
   其中value，里面保存着该学生所有签到的信息
       其中每个签到的信息是字典对象，有两个元素： key 是lessonid的 记录课程id，key是checkintime的 记录签到时间
比如，对于上面的示例中的3条记录，相应的返回结果如下：
{
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],
    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ],
}
'''

dict1 = {}  #外层字典
dict2 = {}  #内层字典
with open(f'/Users/shenyuming/Downloads/sym/tuwen/log.txt') as f:
    list1 = f.read().splitlines()      #读取每一行 ,返回一个list
    for one in list1:
        one1 = one.replace('(','').replace(')','').strip(',')  ##将不需要的符号替换，和去除
        # print(one1)
        checktime,lessonid,uid = one1.split(',')   ##用逗号分隔，将值赋值给三个变量
        # print(checktime,lessonid,uid)
        lessonid = lessonid.strip()       ###去除多余空格
        uid = uid.strip()
        ##将checktime,和 lessonid存入内层字典
        dict2 = {'lessonid':lessonid,'checktime':checktime}
        ##判断用户在不在外层字典中，如果没有生成用户id和空列表的键值对
        if uid not in dict1:
            dict1[uid] = []
        dict1[uid].append(dict2)   ##将内层字典当做外层字典的值传入




import pprint
print(dict1)
pprint.pprint(dict1)
