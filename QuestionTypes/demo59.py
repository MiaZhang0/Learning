#提取url字符串‘https://blog.csdn.net/xufive’中的协议名。
a0 = 'https://blog.csdn.net/xufive'
a1 = a0.split('/',2)
print(a1)
a2 = a1[0][:-1]
print(a2)