#判断集合{‘A’，‘C’}是否是集合{‘D’，‘C’，‘E’，‘A’}的子集
a = {'A','C'}
b = {'D','C','E','A'}
res = a.issubset(b)
print(res)