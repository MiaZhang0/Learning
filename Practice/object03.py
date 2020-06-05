# 多态
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat，也可以接收dog；在其他语言中，如果是猫类只能接收猫类
        # isinstance(obj,类)  判断对象是否是某一类型
        print('{}喜欢养宠物：{}'.format(self.name, pet))


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称：{}，年龄：{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看门')


# 创建对象
cat = Cat('花花', 2)
dog = Dog('123', 1)
person = Person('x')
person.feed_pet('hh')
