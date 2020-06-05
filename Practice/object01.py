# 继承：is a , has a
# 自定义的类都继承了父类object
'''
公路（Road）
    属性：公路名称，公路长度
车（Car）
    属性：车名，时速
方法：1.求车名在哪条公路上以多少的时速行驶了多长，get_time(self,road)
2. 初始化车属性信息__init__方法
3. 打印对象显示车的属性信息
'''
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌，速度：{}'.format(self.brand, self.speed)


# r = Road('京昆高速', 12000)
# aodi = Car('奥迪', 120)
# aodi.get_time(r)
# print(aodi.__str__())
'''
1. has a 一个类中使用了另外一种自定义的类型（如student使用computer和book）
2. 类型：系统类型（str,int,float···），自定义类型（自定义的类）
'''


# 所有自定义的类都是一个类型
class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网····')

    def __str__(self):
        return self.brand + self.type + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + self.author + str(self.number)


class Student:  # has a（包含关系）
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过此书')
                break
            else:
                # 将参数book添加到列表中
                self.books.append(book)
                print('添加成功')

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        # self.name是字符串类型，self.computer是Computer类的类型，self.books是列表类型
        return self.name + str(self.computer) + str(self.books)


# computer = Computer('Mac', 'Mac Pro', '深灰色')
# book = Book('盗墓笔记', '南派三叔', 10)
# stu = Student('zxm', computer, book)
# print(stu)
# book1 = Book('鬼吹灯', '天下霸唱', 10)
# stu.borrow_book(book1)
# stu.show_book()
# book2 = Book('天龙八部', '金庸', 5)
# print(type(book2))  # <class '__main__.Book'>
# stu.borrow_book(book2)
# book3 = Book('红楼梦', '曹雪芹', 3)
# print(book3)
# stu.borrow_book(book3)
# stu.show_book()
'''
继承is a base class 父类  基类
子类中没有的属性会往父类寻找
避免代码冗余
父类中的方法不能满足子类的需求时，需要在子类中定义一个同名方法，称为：重写（优先找子类）
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭····')


class Students(Person):
    def __init__(self, name, age, cla):
        # 调用父类的__init__
        super().__init__(name, age)  # super()表示父类对象
        self.cla = cla

    def study(self, course):
        print('{}正在学{}'.format(self.name, course))


class Doctor(Person):
    def __init__(self, name, age, salary):
        # 调用父类的__init__
        super().__init__(name, age)
        # super(Doctor,self)__init__(name,age)
        self.salary = salary


s = Students('', '', '')
s.eat()
s.study('')
