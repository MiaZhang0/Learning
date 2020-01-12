#以列表形式返回字典{‘Alice’：20，‘Beth’：18，‘Cecil’：21}中所有的键
d = {'Alice':20,'Beth':18,'Cecil':21}
#d.keys()返回的类型是<class 'dict_keys'>，不能使用索引
list = [key for key in d.keys()]
print(list)