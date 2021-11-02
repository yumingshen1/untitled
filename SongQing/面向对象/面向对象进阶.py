'''
面向对象进阶
'''

class Rectangle:
    def __init__(self,weight,height):
        self.weigth = weight    #将传入的参数变为自己的实例，方便同类下的实力方法调用
        self.height = height

    def permiter(self):
        return (self.weigth+self.height)*2

    def area(self):
        return self.height*self.weigth

    @classmethod                ##函数上方加上 @classmethod ,表示该方法是个类方法， 类可以调用它实例也可以调用它，
    def features(cls):
        return '我是类方法'

    @staticmethod              ##在函数上方加上 @staticmethod 表示该方法是普通的静态方法， 类和实例都可以调用
    def fun1(A,B):
        return  A+B

rect = Rectangle(5,7)              ##实例化类 获得对象

print(rect.permiter())          ##实例化的对象调用 实例方法
print(rect.area())

print(rect.features())         ##实例化对象调用 类方法

print(rect.fun1(2,3))           ##实例化的对象调用静态方法，静态方法可以放在类里面也可以不放在类里面，静态方法一般不属于类中，静态方法需要自己传值，

##### print(Rectangle.permiter())   ##使用类直接调用实力方法不可取，需要self,

print(Rectangle.features())     ##使用类直接调用类方法，

print(Rectangle.fun1(5,7))      ##使用类直接调用 静态方法，


'''
通过type()查看对象是方法还是函数, 传入的是类本身，不是类的返回值 ，就是不带（）
'''
print(type(rect.permiter))     ##method
print(type(rect.features))    ##method
print(type(rect.fun1))       ##function

'''
 inspect 判断某个对象是否某种类型, 调用的是方法本身，不是返回值，传入不带()，返回布尔值
'''
import inspect

print(inspect.ismethod(rect.permiter))
print(inspect.ismethod(rect.features))
print(inspect.isfunction(rect.fun1))


'''
    继承
'''
##完全继承

class Square(Rectangle):  ##直接继承父类 ， 方法不做改变
    pass

squ = Square(2,3)           ##实例化子类
print(squ.permiter())       ##调用父类的实例方法
print(squ.features())       ##调用父类的类方法
print(squ.fun1(2,2))        ##调用父类的静态方法


##部分继承

class Reques(Rectangle):
    def __init__(self,dist):        ##父类是两个参数， 子类想用一个参数， 重写初始化方法传入一个参数，用父类的参数将子类传入的参数变为自己的实例
        self.weigth = dist
        self.height = dist
req = Reques(10)
print(req.permiter())
print(req.area())
print(req.features())
print(req.fun1(10,12))

##继承父类时，想扩展一些方法

class Quest(Rectangle):
    def __init__(self,dist):    ##修改传入的参数数量，
        self.weigth = dist        ##使用父类的初始化值来初始化子类的参数为自己的实例
        self.height = dist

    def features(cls):
        super().features()      ##通过super()获得父类的features()的代码信息
        return cls.weigth+cls.height

que = Quest(20)
print(que.permiter())
print(que.features())


'''
property 声明下面的方法是属性，而不是方法 ，  调用的时候可以调用方法本身， 不要调用返回值否则会提示str object不可调用
'''
class test1:
    def __init__(self):
        pass
    @property
    def fun2(self):
        return 'aaa'
tt = test1()
## print(tt.fun2())  ##会提示str object 不可调用
print(tt.fun2)   ##直接调用方法本身可以

