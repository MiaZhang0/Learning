#将三个字符串‘15’，‘127’，‘65535’左侧补0成同样长度
a = ['15','127','65535']
len_max = max([len(item) for item in a])
for item in a:
    print(item.zfill(len_max))