'''
私有属性或私有方法不能被外部调用，也不能被子类调用
在属性或方法的前面加上 __，就变成了私有属性或私有方法
'''

class Class_test1:
    __str1='ABC'   ##私有属性
    str1 = 'EDF'
    def __init__(self):
        pass
    def __method1(self):    #私有方法
        print('这是私有方法')

    def method2(self):          ##私有属性和方法，可以放到对外开放的方法中，可以调用该方法获取私有属性和方法。该函数调用私有属性和方法
        print(self.__str1)      ##调用私有属性
        self.__method1()        ##调用私有方法

cls1 = Class_test1()         ##实例化类

# print(cls1.__str1)         ##私有属性不能被外部调用
# print(cls1.__method1())     ##私有方法不能被外部调用

cls1.method2()          ##调用私有属性和私有方法


'''
所有的类都是object子类，无论是否声明继承，实际都是继承的
'''
class Class_test2:
    '''
    1234
    '''
    pass
print(Class_test2.__dict__)         ##类的属性
print(Class_test2.__doc__)          ##类的注释 ， 类和方法的注释建议用''' '''，这样可以用 __doc__查到
print(Class_test2.__name__)         ##类的名称
print(Class_test2.__base__)         ##类的父类，显示第一个父类
print(Class_test2.__bases__)        ##类的所有父类，显示类的所有的父类


'''
多继承
'''
class Money1:
    def money1(self):
        print('一亿人民币')

class Money2:
    def money2(self):
        print('两亿人民币')
class human(Money1,Money2):     ##如果继承多个父类，按顺序用逗号分割， 如果两个父类中有相同名字的方法时，按继承顺序取值第一个
    pass
hm = human()    ##实例化
hm.money1()     ##调用父类1的方法
hm.money2()     ##调用父类2的方法
print(human.__bases__)          ##查询该类的所有父类。


'''
多态
'''
class Dog:
    def say(self):
        print('狗叫声')
class Cat:
    def say(self):
        print('猫叫声')
dog = Dog()
cat = Cat()

def animal_say(obj):    ##封装函数，传值，掉不同的类
    obj.say()
animal_say(dog)
