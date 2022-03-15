
'''
##单例模式
'''

###一般情况下类可以实例化多个，单例模式只有一个

class Single():
    def __init__(self,*args):   ##初始化方法
        pass
    def __new__(cls, *args, **kwargs):     ##构造方法，用于生成实例
        if not hasattr(cls,'obj'):        ##hasattr(对象,属性或方法) 判断类中有没有实例化方法，没有则新建
            cls.obj = object.__new__()     ##新建实例化对象
        else:
            return cls.obj              ###如果类中有实例化对象，直接返回实例


'''
反射 ， hasattr \ getattr \  setattr
'''

class Fanguan:
    price = 20   ##类(实例化后的对象)的属性
    def yu(self):
        return '鱼'
    def ji(self):
        return '鸡'
    def ya(self):
        return '鸭'
fg = Fanguan()  ##实例化，  即使类创建是没有(), 在调用进行实例化的时候也要加上(),才是实例化


##  hasattr(对象,属性) 判断对象中是否有某个方法或属性
while True:
    inp = input('请输入菜单：')
    if hasattr(fg,inp):     ##hasattr(对象,属性或方法) 判断对象中时候有某个方法或属性
        print('好的，请稍等')
        break
    else:
        print('sorry!')


### getattr (对象，属性或方法，缺省值) ，判断对象中是否有某个方法或属性，有就返回，没有就返回缺省值
def fun1():
    return '我是缺省值'

inp2 = input('请输入吧：')
c = getattr(fg,inp2,fun1)
print(c())


### setattr(对象，属性或方法，新值)
print(fg.price)    #对象的属性，还没修改
setattr(fg,'price',22)    ##将对象中的price 值 修改为22
print(fg.price)    ##对象的属性，修改后的值

