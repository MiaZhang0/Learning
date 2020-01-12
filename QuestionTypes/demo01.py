#将元祖（1,2,3,）和集合{4,5,6}合并成一个列表
tuple = (1,2,3)
set = {4,5,6}
list = list(tuple) + list(set)
print(list)