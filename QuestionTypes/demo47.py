#判断字符串‘this is python’是否以‘this’开头，又是否以‘python’结尾
s = 'this is python'
res1 = s.startswith('this')
print(res1)
res2 = s.endswith('python')
print(res2)