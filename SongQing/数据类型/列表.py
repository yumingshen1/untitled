listq = [1,2,'a','r',(1,2,3,4,5),{'as':'kl'}]
print(listq)
listq.append(600)
print(listq)
listq.insert(2,'测试')
print(listq)

listw = [1,3,4,6,7,'cks',(0,6,4,6,7)]

listq.extend(listw)
print(listq)
print(listq.pop(-1)) #下标
listq.remove(2)  #删除值，不是下标
print(listq)


##元组
tuple1 = (1,2,3)
tuple2 = (20,)
print(tuple1,tuple2)
tuple3 = (22,23,55,[2,50])  ##元祖中的列表值可以修改
tuple3[3][1] = 60
print(tuple3)


##深拷贝，浅拷贝
##赋值       -------->   list是可变的，是同一个列表，改边后会同时改变
list5 = [100,200,300,[500,600]]
list5_new = list5
list5[1] = 220
print(list5,id(list5))
print(list5_new,id(list5_new))

##浅拷贝  ---- >  生成一个新的对象， 但是子列表仍然是同一个
import copy
print('----浅拷贝---')
list5_new=copy.copy(list5)
list5[1] = 230
list5[3][1] = 650  #子列表的值还是同一个
print(list5,id(list5))
print(list5_new,id(list5_new))

print('---深拷贝---')
##深拷贝    ------ > 生成一个新的对象，子列表也是新的对象
list5_new2 = copy.deepcopy(list5)
list5[1] = 130
list5[3][1] = 700
print(list5,id(list5))
print(list5_new2,id(list5_new2))

print('-----切片-----')
##切片等价于浅拷贝，
list5_new3 = list5[:]
list5[2] = 707
list5[3][1] = 909
print(list5,id(list5))
print(list5_new3,id(list5_new3))

