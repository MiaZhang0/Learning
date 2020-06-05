# 递归函数：函数自己调自己
'''
普通函数：def func(): pass
匿名函数： lambda 参数：返回结果
递归函数：普通函数的一种表现形式
嵌套函数---》闭包---》装饰器

递归函数的特点：1.必须有终点；2.有一个入口
'''


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)
print(result)

# 等价于1-10的累加
s = 0
for i in range(11):
    s += i
print(s)

