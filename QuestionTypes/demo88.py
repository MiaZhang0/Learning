#数字列表求和
import random

#使用 random 函数生成5 个随机数
a = [random.random() for i in range(5)]
print(a)
print(sum(a))