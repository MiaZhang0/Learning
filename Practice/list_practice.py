# 列表推导式  字典推导式  集合推导式
# 1. 列表推导式：【表达式 for 变量 in 旧列表】 或者 【表达式 for 变量 in 旧列表 if 条件】
# 过滤长度小于或者等于3的人名，一层循环
names = ['tom','lily','Lucy','Jack','Bob','h']
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 元组列表：0~5的偶数，0~10的奇数【（0,1），（0,3），（0,5），···】，两层循环
result1 = [(x,y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(result1)

# 取出list中的3,6,9,5构成新列表【3,6,9,5】，没有条件
list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
newlist = [i[-1] for i in list]
print(newlist)

# if ··· else ···列表推导式
dict1 = {'name':'tom','salary':5000}
dict2 = {'name':'lucy','salary':8000}
dict3 = {'name':'jack','salary':4000}
dict4 = {'name':'lily','salary':3000}
list1 = [dict1,dict2,dict3,dict4]
# 薪资大于5000加200，小于等于5000加500
newlist1 = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]
print(newlist1)

# 集合推导式
list2 = [1,3,5,7,8,9,0]
set = {x + 1 for x in list2 if x < 5}
print(set)

# 字典推导式
dict = {'a':'A','b':'B','c':'C','d':'C'}
newdict = {value:key for key,value in dict.items()}
print(newdict)