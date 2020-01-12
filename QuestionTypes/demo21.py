#以列表形式返回字典{‘Alice’：20，‘Beth’：18，‘Cecil’：21}中所有键值对组成的元组
d = {'Alice':20,'Beth':18,'Cecil':21}
list = [key for key in d.items()]
print(list)