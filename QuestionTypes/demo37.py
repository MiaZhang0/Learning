#返回集合{‘A’，‘D’，‘B’}中未出现在集合{‘D’，‘E’，‘C’}中的元素（差集）
a = {'A','D','B'}
b = {'D','E','C'}
res1 = a.difference(b)
print(res1)
res2 = a - b
print(res2)
