#以列表形式返回字典{‘Alice’：20，‘Beth’：18，‘Cecil’：21}中所有的值
d = {'Alice':20,'Beth':18,'Cecil':21}
#d.values返回额类型是<class 'dict_values'>,不能使用索引
list = [key for key in d.values()]
print(list)