#返回两个集合{‘A’，‘D’，‘B’}和{‘D’，‘E’，‘C’}的并集
a = {'A','D','B'}
b = {'D','E','C'}
res = a.union(b)
print(res)
#并集不能用a + b