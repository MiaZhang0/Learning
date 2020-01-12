#将列表[3,0,8,5,7]中大于5元素置为1，其余元素置为0
list = [1 if item>5 else 0 for item in[3,0,8,5,7]]
print(list)