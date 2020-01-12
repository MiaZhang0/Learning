#反转列表[0,1,2,3,4,5,6,7]后给出元素5的索引号
list = [0,1,2,3,4,5,6,7]
#反转list
new_list = list[::-1]
#新列表中元素5的索引号
print(new_list.index(5))