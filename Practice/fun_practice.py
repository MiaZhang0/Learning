# 求列表中的最大值,iterable可迭代對象
# def max(iterable):
#     # 假設第一個為最大值
#     max = iterable[0]
#     for i in iterable:
#         if i > max:
#             max = i
#     print('最大值是：', max)


# isinstance()判斷是不是XX類型
max([1, 2, 3, 4, 5, 7, 8])

# 自定義enumerate函數
# def enumerate(s):
#     list = []
#     index = 0
#     for i in s:
#         t = (index, i)
#         list.append(t)
#         index += 1
#     print(list)


s = {1, 3, 5, 6, 7, 45, 89, 9, 0}

# 1. 可變參數：*args表示傳入任意多個參數，且可變參數必須放在不可變參數的後面，默认返回的是元组
# def add1(*args):
#     print(args)
# add1(1, 2)

# 2. 关键字参数：key = value, 此时表示默认值
# def add2(a, b=10, c=5):
#     result = a + b + c
#     print(result)
# add2(1, 7)
# add2(2, c=8)

# 3. 打印每位同学的年龄和姓名
# students = {'001': ('蔡徐坤', 21), '002': ('王源', 19), '003': ('王俊凯', 20), '004': ('易烊千玺', 19)}
# def print_boy(persons):
#     if isinstance(persons, dict):
#         values = persons.values()
#         # print(values)
#         for name, age in persons.values():
#             print('{}的年龄是{}'.format(name, age))
# print_boy(students)


# def func(**kwargs): # 可变参数--关键字参数，调用时的赋值方式是 key = value，默认返回的是字典
#     # 传递实参时，**变量名，将字典进行拆包，拆成关键字参数的形式
#     print(kwargs)
# # 调用时需要将字典变量进行拆包即用**
# func(**students)

# 4. return返回值可以返回多个，且是元组类型
# def add3(a,b):
#     result = a + b
#     return result

'''
加入购物车
判断用户是否登录，如果登录，成功加入购物车，否则提示请登录之后添加
'''
# def add_shoppingcart(goodsName):
#     # 判断是否有商品
#     # 如果有
#     if goodsName:
#         print('成功将{}加入购物车'.format(goodsName))
#     else:
#         print('没有选中任何商品')
#
# def login(user,pwd):
#     if user == 'zxm' and pwd == '123':
#         print('登录成功')
#         return True
#     else:
#         print('用户名或者密码错误')
#         return False
#
# user = input('请输入用户名：')
# pwd = input('请输入密码：')
# islogin = login(user,pwd)
# # 如果登录成功，执行添加商品
# if islogin:
#     # 添加商品到购物车
#     add_shoppingcart('口红')
# # 没有登录
# else:
#     answer = input('登录成功之后才能添加商品，是否重新登录?（y/n）')
#     if answer == 'y':
#         user = input('请输入用户名：')
#         pwd = input('请输入密码：')
#         login(user,pwd)
#         add_shoppingcart('口红')

'''
用户登录，输入用户名，密码，验证码
'''
import random


# 生成验证码
def generate_checkcode(n):
    code = ''
    s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    for i in range(n):
        ran = random.randint(0,len(s)-1)
        code += s[ran]
    return code


def login():
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    # 获取验证码
    code = generate_checkcode(4)
    print('验证码是：', code)
    in_code = input('请输入验证码：')
    if in_code.lower() == code.lower():
        # 验证码输入正确
        if user == 'zxm' and pwd == '123':
            print('登录成功')
        else:
            print('用户名或者密码错误')
    else:
        print('验证码输入错误')


login()

# 内部函数，函数的嵌套
def func():
    # 声明变量
    n = 1
    list = [0,2,4,1,3,6,3,9]
    # 声明内部函数
    def inner_func():
        pass
'''
内部函数可以修改外部函数的可变类型的变量
内部函数修改全局的不可变变量时，需要在内部函数声明global 变量名
内部函数修改外部函数的不可变的变量时，需要在内部函数中声明：nonlocal 变量名
使用locals()函数进行查看当前函数中声明的内容有哪些，返回的是字典类型
使用globals()函数进行查看所有全局变量
'''

