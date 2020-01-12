#若a = dict()，令b = a，执行b.update({‘x’：1})，a已被改变。为何？如何避免？
a1 = dict()
#对象a 和对象b在内存中是同一个，所以会出现关联
b = a1
b.update({'x':1})
print(a1)
print(id(a1))
print(id(b))

a2 = dict()
#正确的做法是复制一个新的对象
c = a2.copy()
c.update({'x':1})
print(a2)
print(id(a2))
print(id(c))
