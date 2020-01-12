#删除列表中索引号为奇数（或偶数）的元素
a = list(range(10))
print(a)
#删除列表中的偶数
del a[::2]
print(a)

b = list(range(10))
#删除列表中的奇数
del b[1::2]
print(b)
