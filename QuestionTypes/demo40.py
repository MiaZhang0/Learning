#返回两个集合{‘A’，‘D’，‘B’}和{‘D’，‘E’，‘C’}未重复的元素的集合
a = {'A','D','B'}
b = {'D','E','C'}
res = a.symmetric_difference(b)  #返回 a和b 非重复元素的集合
print(res)