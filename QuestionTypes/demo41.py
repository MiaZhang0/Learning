#判断两个集合{‘A’，‘D’，‘B’}和{‘D’，‘E’，‘C’}是否有重复元素
a = {'A','D','B'}
b = {'D','E','C'}
#判断 a和b 是否不包含相同的元素，如果没有，则返回True，有，则返回False
res1 = a.isdisjoint(b)
print(res1)
#取反才是本题的正确答案
res2 = not a.isdisjoint(b)
print(res2)
