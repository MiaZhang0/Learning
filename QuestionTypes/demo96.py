#使用map 函数求列表[2,3,4,5]中每个元素的立方根
list = [item for item in map(lambda x:pow(x,1/3),[2,3,4,5])]
print(list)