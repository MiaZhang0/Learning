# 闭包closure的概念
'''
1. 外部函数中定义了内部函数
2. 外部函数有返回值，且返回值是：内部函数名
3. 内部函数中引用外部函数的变量
def 外部函数()：
    变量1···
    def 内部函数():
        引用变量1···
    return 内部函数
'''


def func(a, b):
    c = 10

    def inner_func():
        # 此处引用外部函数变量c
        s = a + b + c
        print('相加之后的结果是：', s)

    return inner_func


# ifunc == inner_func,
ifunc = func(1, 2)
ifunc()

# 闭包的应用
'''
1. 保存返回闭包时的状态（不会受到外界参数的影响）
2. 读取其他元素的内部变量
3. 延长作用域
'''
# 闭包的缺点
'''
1. 作用域没有那么直观
2. 因为变量不会被垃圾回收，所以有一定的内存占用问题
'''
# 闭包总结
'''
1. 闭包优化了变量，原来需要类对象完成的工作，闭包可以完成
2. 由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3. 闭包的好处，使代码变得简洁，便于阅读代码
4. 闭包是理解装饰器的基础
'''
# 计数器
def generate_count():
    container = [0]
    def add_one():
        container[0] += 1
        print('当前是第{}次访问'.format(container[0]))
    return add_one
counter = generate_count()
counter()