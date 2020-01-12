#向子典{‘Alice’：20，‘Beth’：18，‘Cecil’：21}中追加 ‘David’：19键值对，更新Cecil的值为17.
d = {'Alice':20,'Beth':18,'Cecil':21}
d.update({'David':19})
d.update({'Cecil':17})
print(d)