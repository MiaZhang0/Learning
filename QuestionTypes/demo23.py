#删除字典{‘Alice’：20，‘Beth’：18，‘Cecil’：21}中的Beth键后，清空该字典
d = {'Alice':20,'Beth':18,'Cecil':21}
d.pop('Beth')
print(d)
d.clear()
print(d)