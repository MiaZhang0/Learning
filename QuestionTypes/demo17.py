#若a = [1,2,3]，令 b = a，执行b[0] = 9，a[0]亦被改变。为何？如何避免？
a1 = [1,2,3]
b = a1
b[0] = 9
print(a1)  #对象 a 和对象 b 在内存中是同一个，所以会出现关联
print(id(a1))
print(id(b))
#正确的做法是复制一个新的对象
a2 = [1,2,3]
c = a2.copy()
c[0] =9
print(c)
print(id(a2))
print(id(c))
