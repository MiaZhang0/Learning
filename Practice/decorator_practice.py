# 装饰器
# 应用场景：将商品加入购物车，登录后才能加入；付款，修改收货地址····，此处需要判断用户的登录状态
# 装饰器的特点
'''
1. 函数A是作为参数出现的（函数B是接收函数A作为参数）
2. 有闭包的特点

'''


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        for i in range(number):
            a += 1
        print('修改后的a：', a)

    return inner_func()


# 调用
# f = func(5)
# f()

# 定义一个装饰器
def decorator(f):
    a = 100
    print('wrapper外层打印测试····')

    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('------------->刷漆')
        print('-------------->铺地板')

    print('wrapper加载完成')
    print(f)  # <function house at 0x0000027CC7647620>
    print(wrapper)  # <function decorator.<locals>.wrapper at 0x000001EDD5A476A8>
    return wrapper


# 调用装饰器
# 装饰器的功能
'''
1. house被装饰函数
2. 将被装饰函数作为参数传给装饰器decorator,即执行 f = house()
3. 执行decorator函数
4. 将返回值又赋值给house，house = wrapper,因此最后调用house实际是调用wrapper
'''


@decorator
def house(address, name, age=10):
    print('我是{},我在{}，我的年龄是{}'.format(name, address, age))


# 执行报错：TypeError: 'NoneType' object is not callable
# house()
# 解决方法：调用函数时去掉括号
print(house)
house('天府五街', 'AA', age=15)


# 多层装饰器,就近原则，先装近再装远
def zhuang1(f):
    print('-------->1,start')

    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('------------->刷漆')

    print('-------->1,end')
    return wrapper


def zhuang2(f):
    print('-------->2,start')

    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('------------->地板')

    print('-------->2,end')
    return wrapper


@zhuang2
@zhuang1
def house1():
    print('------>house1')


house1()

# 装饰器中带参数
'''
1. 带参数的装饰器是三层的
2. 最外层的函数负责接收装饰器的参数
3. 里面的内容还是原装饰器的内容
'''


def outer(a):
    def decorator1(f):
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
            print('------------->地板{}块'.format(a))

        return wrapper

    return decorator1


@outer(10)
def house2():
    print('-------->house2')


house2()
