'''
编写一个简单的工资管理程序，系统可以管理以下四类人：工人（worker），销售员（salesman），经理（manager），销售经理（salesmanager）
所有员工都有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
（1）工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
（2）销售员：具有销售额和提成成比例的属性，工资计算方法为销售额*提成比例
（3）经理：具有固定月薪的属性，工资计算方法为固定月薪
（3）销售经理：工资计算方法为销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
（1）添加所有类型的人员
（2）计算月薪
（3）显示所有人工资情况

'''


class Person:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号：{}，姓名：{}，薪资：{}'.format(self.id, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, id, name, salary, hours, wage):
        super().__init__(id, name, salary)
        self.hours = hours
        self.wage = wage

    def getSalary(self):
        salary = self.hours * self.wage
        self.salary += salary
        return self.salary


class Salesman(Person):
    def __init__(self, id, name, salary, sales, percent):
        super().__init__(id, name, salary)
        self.sales = sales
        self.percent = percent

    def getSalary(self):
        salary = self.sales * self.percent
        self.salary += salary
        return self.salary


# 多继承（一个子类可能有多个父类）
# 多继承的搜索顺序：经典类 新式类
# 经典类：从左至右，深度优先（python2.x）；新式类：广度优先（python3.x）
import inspect


class Base:
    def test(self):
        print('---Base---')


class A(Base):
    def test(self):
        print('AAAAAAAAA')


class B(Base):
    def test(self):
        print('BBBBBBBB')


class C(Base):
    def test(self):
        print('CCCCCCCCCC')


class D(A, B, C):
    def test(self):
        print('DDDDDDDDDD')


print(inspect.getmro(D))
print(D.__mro__)
