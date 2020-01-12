#从列表[True，1,0，‘x’，None，‘x’，False，2，True]中删除元素‘x’
list = [True,1,0,'x',None,'x',False,2,True]
for i in range(list.count('x')):
    list.remove('x')
print(list)

