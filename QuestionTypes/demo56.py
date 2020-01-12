#将三个全英文字符串（比如，‘ok’，‘hello’，‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果
a = ['ok','hello','thank you']
#len_max为最长字符串的长度
len_max = max([len(item) for item in a])
for item in a:
    print('"%s"'%item.ljust((len_max)))
print('------------------------------------')
for item in a:
    print('"%s"'%item.rjust(len_max))
print('-------------------------------------')
for item in a:
    print('"%s"'%item.center((len_max)))
