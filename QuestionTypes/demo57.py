#将三个字符串（比如，‘Hello，我是David’，‘OK，好’，‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果。
a = ['Hello，我是David','OK，好','很高兴认识你']
#各字符串长度
a_len = [len(item) for item in a]
#各字符串gbk编码的字节码长度
a_len_gbk = [len(item.encode('gbk')) for item in a]
#各字符串包含的中文符号个数
c_num = [a-b for a,b in zip(a_len_gbk,a_len)]
#最大字符串占位长度
len_max = max(a_len_gbk)
for s,c in zip(a,c_num):
    print('"%s"'%s.ljust(len_max-c))
print('---------------------------------------------')
for s,c in zip(a,c_num):
    print('"%s"'%s.rjust(len_max-c))
print('-------------------------------------------------')
for s,c in zip(a,c_num):
    print('"%s"'%s.center(len_max-c))
