#删除集合{‘x’，‘y’，‘z’}中的‘z’元素，增加元素‘w’，然后清空整个集合
a = {'x','y','z'}
a.remove('z')
print(a)
a.add('w')
print(a)
a.clear()
print(a)