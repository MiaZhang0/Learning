# 匿名函数：简化函数定义
# 格式： lambda 参数1，参数2,····

s = lambda a, b: a + b


# 等价于
def f(a, b):
    s = a + b
    return s


# 匿名函数可以作为参数传递
def func(x, y, f):
    print(x, y)
    print(f)
    s = f(x, y)
    print(s)


func(1, 2, lambda a, b: a + b)

# 内置函数+ 匿名函数
list0 = [{'a': 10, 'b': 20}, {'a': 11, 'b': 22}, {'a': 12, 'b': 20}]

m = max(list0, key=lambda x: x['a'])
print(m)

list1 = [2, 3, 5, 6, 7, 8, 9, 0, 11]
# map()函数：对列表中的元素作统一操作，返回的是多个值，有多少个元素返回多少个值
result = map(lambda x: x + 2, list1)
print(list(result))

func = lambda x: x if x % 2 == 0 else x + 1
result1 = func(5)

result2 = map(func, list1)

print(list(result2))

for index, i in enumerate(list1):
    if i % 2 != 0:
        list1[index] = i + 1
print(list1)

# reduce()：对列表中的元素进行加减乘除运算的函数，返回的是一个值
from functools import reduce

tuple = (2, 3, 5, 6, 8, 9, 0)
result3 = reduce(lambda x, y: x + y, tuple, 10)  # initial = 10 初始值
print(result3)

# filter()过滤函数，相当于自定义的func()函数
# 找出list1中大于10的元素
result4 = filter(lambda x: x > 10, list1)
print(list(result4))


def func(list):
    list2 = []
    for i in list:
        if i > 10:
            list2.append(i)
    return list2
print(func(list1))

students = [{'name':'Tom','age':20},{'name':'Lucy','age':19},{'name':'Lily','age':13},{'name':'Jack','age':30}]
# 找出students中年龄大于20的学生
result5 = filter(lambda x:x['age'] > 20,students)
print(list(result5))

# sorted()函数，按照年龄从小到大排序，reverse=true倒序
students1 = sorted(students,key=lambda x:x['age'],reverse=True)
print(students1)

