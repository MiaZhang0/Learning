# 集合的应用
import random

# 1. 去重
list = [1, 1, 1, 4, 5, 6, 7, 8, 6, 6, 6, 0]
# print(set(list))
s0 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(id(s0))
s0.add(11)
print(s0)
print(id(s0))
set1 = set()
for i in range(10):
    ran = random.randint(1, 20)
    set1.add(ran)
print(set1)
num = int(input('输入一个数字：'))
set1.discard(num)
print(set1)

# 对称差集

set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = {4, 5, 6, 0, 9, 1, 2, 4, 6}

# symmetric_difference()
result = (set2 | set3) - (set2 & set3)
print(result)
result2 = set2 ^ set3
print(result2)

