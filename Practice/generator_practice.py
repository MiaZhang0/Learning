'''
通过列表推导式，我们可以直接创建一个列表
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，会占用很大的存储空间。
如果我们仅需要访问前面几个元素，那后面绝大多数元素占用的空间就浪费了。
所以，如果列表元素可以按照某种算法推算出来，我们是否可以在循环过程中不断推算出后续的元素？
这样就不必创建完整的list，从而节省空间。在python中，这种一边循环一边计算的机制，称为生成器（generator）。

得到生成器的方式：
1. 通过列表推导式得到生成器
2. 通过调用 生成器名称.__next__ 方式得到元素
3. 通过调用系统内置函数next(生成器名称)
4. 借助函数生成（斐波那契数列）
备注：函数中有关键字yield，此时的函数就是生成器而非函数
步骤：
（1）自定义一个函数，且加入关键字yield（return + 暂停）
（2）接收返回值
（3）调用next()或者__next__(),获取元素
（4）send(value): 向生成器中传值，第一次调用send(None)

生成器的应用场景：协程（一个线程中有多个任务），多个协程交替执行
（进程，线程，协程）
'''

# g = (x * 3 for x in range(10))
# print(g)
# print(type(g))
# # 调用一次仅得到一个元素
# print(g.__next__())
# print(next(g))

# 斐波那契数列
# def fib(length):
#     a, b = 0, 1
#     n = 0
#     while n < length:
#         yield b
#         a, b = b, a + b
#         n += 1
#     # return '元素加载完毕'

# g = fib(8)
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('元素加载完毕')
#         break

# 多协程
def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield None


def task2(n):
    for i in range(n):
        print('正在唱第{}首歌'.format(i))
        yield None


g1 = task1(5)
g2 = task2(5)
while True:
    try:
        e1 = next(g1)
        e2 = next(g2)
    except:
        print('元素加载完毕')
        break
