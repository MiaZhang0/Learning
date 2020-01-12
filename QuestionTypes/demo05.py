#分别统计列表[True，False，0,1,2]中True，False，0,1,2的元素个数，发现了什么？
list = [True,False,0,1,2]
a = list.count(True)
b = list.count(False)
c = list.count(0)
d = list.count(1)
e = list.count(2)
print(a,b,c,d,e)
#结果为2,2,2,2,1
#count（）不区分True和1，False和0，但None、‘’不会被视为False