'''
面向对象的优点：模块化封装（类，对象，属性，方法），复用性与灵活性比面向过程好，可以针对部分作修改，不影响整个过程。
类的定义：class 类名():
            特征：属性
            动作：方法
属性的定义：分为类属性和对象属性，在调用时，先找对象属性再找类属性
实例化对象：对象 = 类名()
创建对象属性：对象.属性名 = value
类中的方法：普通方法（def 方法名(参数)），类方法，静态方法，魔术方法__名字__()

魔术方法：自动触发
（1）__init__():初始化魔术方法
实例化对象时，会先执行__init__，再将内存地址赋值给对象，作用：动态给self空间添加属性（self是一个动态的内存地址），这些属性必是共性。
（2）__new__()：实例化的魔术方法，向内存申请空间用，在类中，先执行new，再执行init
（3）__call__()：对象调用魔术方法，将对象当函数用时，需要call函数并默认调用它
（4）__del__()：析构器，可以将对象赋值给多个变量，每个变量的地址都是一样的；del用于删除这些变量；
查看对地址引用的次数，即变量的个数import sys  sys.getrefcount();
如果这些变量被删完后，会默认执行del。
（5）__str__()：打印对象名称时自动触发，调用str里面的内容，需要加return

类方法：没有对象也可以调用（不用将类实例化）；
（1）定义需要依赖装饰器@classmethod，
（2）类方法中的参数不是一个对象，是一个类，
（3）类方法中只能使用类属性，
（4）类方法中不能使用普通方法；类中方法的调用，需要依赖self对象
@classmethod
def test(cls):
   print(cls)
类方法的作用：
在创建对象之前，需要完成的一些功能

静态方法：
（1）需要装饰器@staticmethod
（2）静态方法无需传递参数
（3）只能访问类的属性和方法，对象的是无法访问的
（4）加载时机同类方法

@staticmethod
def test():
    pass

'''


class Person:
    __age = 18  # 私有化变量（类之外不可以修改）

    def __init__(self, name):
        self.name = name

    def show(self):
        print('*****')

    @classmethod
    def update_age(cls):
        cls.__age = 20

    @classmethod
    def show_age(cls):
        print(cls.__age)

    @staticmethod
    def test():
        print('&&&&&&&')


# 调用类方法与静态方法，不需要依赖对象，不需要实例化对象
Person.update_age()
Person.show_age()
Person.test()

# 调用普通方法，需要实例化对象
p = Person('')
p.show()
'''
1. 封装
（1）私有化属性（只能在类中修改） __变量名（属性） = value
（2）定义共有set（赋值用）和get（取值用）方法
A:赋值
def setAge(self,age):
    self.__age = age
B:取值
def getAge(self):
    return self.__age
（3）特点：隐藏属性不被外界随意更改，通过set赋值修改；获取某个具体属性使用get实现
2. 继承
3. 多态
'''


class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 必须先有getXXX
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖get
    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('不在指定范围')

    # def setAge(self,age):
    #     self.__age = age
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.__age)


P = People('zxm', 18)
print(P.__str__())
P.name = 'ZXM'
P.age = 20
print(P.__str__())