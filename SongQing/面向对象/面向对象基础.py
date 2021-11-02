##面向对象

class Rectangle:
    list1 = [1, 3, 5, 10, 20]
    def __init__(self,weight,height):  ##初始化函数， 初始化方法中传入需要的参数
        self.weight = weight      ##将参数转为自身的，使得该class下的所有函数均可使用
        self.height = height
        self.list2 = [10,20,33,40,50]
    def zhouchang(self):
        return (self.weight+self.height)*2
    def mianji(self):
        return self.weight*self.height

##调用类里面的函数，必须先实例化类，才能调用里面的方法
rect = Rectangle(3,3)    #调用函数需要补全()
rect2 = Rectangle(5,6)
print(rect.zhouchang())
print(rect.mianji())
print(rect.__dict__)    #查看实例的属性

print(id(rect.list1)==id(rect2.list1))  #list1 类属性，唯一，所有实例共用的一个list1
print(id(rect.list2)==id(rect2.list2))   ##list, 实例属性，不唯一， 每个实例有自己的属性




