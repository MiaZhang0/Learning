#将列表[0,1,2,3.14,‘x’，None，‘ ’，list()，{5}]中各个元素转为布尔型。
list = [bool(item) for item in [0,1,2,3.14,'x',None,'',list(),{5}]]
print(list)